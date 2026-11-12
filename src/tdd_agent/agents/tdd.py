"""TDD agent: builds the class one method at a time, red -> code -> green (ADR 012).

For each method (helpers before the methods that call them):
    1. add the method's tests to the suite
    2. RED:   run the suite on the current code (the method isn't implemented yet)
    3. CODE:  the LLM implements the method, seeing the code, the suite and the red result
              (skipped if the suite is already green: no failing test, no new code)
    4. GREEN: run the whole suite (this method's tests + all earlier ones = regression)
              if red: send the failures back, up to max_fix_attempts times, then move on anyway
"""

from pydantic import BaseModel

from tdd_agent.agents.interface import AgentResult
from tdd_agent.dataset import clean_skeleton, methods_in_order, test_header, tests_for_method
from tdd_agent.grading.parser import TestCounts, parse_log
from tdd_agent.grading.runner import RunOutput, run_tests
from tdd_agent.llm import LLM, LLMCall, extract_code
from tdd_agent.prompts import CODER_SYSTEM, TDD_FIX, TDD_IMPLEMENT

SEPARATOR = "=" * 70  # unittest prints this above each failure
MAX_FEEDBACK_CHARS = 4000  # cap on the test output sent back to the LLM


class MethodStep(BaseModel):
    """What happened for one method; saved to steps/<task_id>.json."""

    method: str
    tests_in_suite: int  # tests run at this step (this method's + earlier ones)
    red_passed: int  # before implementing: tests already passing
    coded: bool  # False when the suite was already green, so no code was written
    fix_attempts: int  # extra calls after the first implementation
    green_passed: int  # after the last attempt
    green: bool  # whole suite passing at the end of this step


def feedback(run: RunOutput, counts: TestCounts) -> str:
    """The part of the test output the LLM needs: the summary and the failures."""
    if run.timed_out:
        return "The tests timed out (possible infinite loop or very slow code)."
    if counts.tests_total == 0:  # crashed before any test ran, e.g. a SyntaxError
        return "The tests could not run:\n" + run.log[-MAX_FEEDBACK_CHARS:]
    summary = f"{counts.tests_passed} of {counts.tests_total} tests pass."
    if counts.tests_passed == counts.tests_total:
        return summary
    failures = SEPARATOR + SEPARATOR.join(run.log.split(SEPARATOR)[1:])
    return summary + "\n\n" + failures[:MAX_FEEDBACK_CHARS]


class TDDAgent:
    name = "tdd"

    def __init__(self, llm: LLM, max_fix_attempts: int = 3, run=run_tests):
        self.llm = llm
        self.max_fix_attempts = max_fix_attempts
        self.run = run  # injected, like the LLM: a test can pass a fake runner

    def _run_suite(self, code: str, suite: str) -> tuple[RunOutput, TestCounts]:
        run = self.run(code, suite)
        return run, parse_log(run.log)

    def _ask(self, prompt: str, calls: list[LLMCall]) -> str:
        call = self.llm.call(CODER_SYSTEM, prompt)
        calls.append(call)
        return extract_code(call.reply)

    def generate(self, task: dict) -> AgentResult:
        code = clean_skeleton(task)
        suite = test_header(task)
        calls: list[LLMCall] = []
        steps: list[dict] = []

        for method in methods_in_order(task):
            name = method["method_name"]
            suite += "\n\n" + tests_for_method(task, method)

            # RED: the suite on the current code, before this method is implemented
            run, counts = self._run_suite(code, suite)
            red_passed = counts.tests_passed

            if self._passed(run, counts):  # already green: TDD writes no code without a failing test
                steps.append(
                    MethodStep(
                        method=name,
                        tests_in_suite=counts.tests_total,
                        red_passed=red_passed,
                        coded=False,
                        fix_attempts=0,
                        green_passed=counts.tests_passed,
                        green=True,
                    ).model_dump()
                )
                continue

            # CODE: implement the method
            code = self._ask(
                TDD_IMPLEMENT.format(code=code, method=name, tests=suite, feedback=feedback(run, counts)),
                calls,
            )

            # GREEN: the whole suite; fix until it passes or the attempts run out
            run, counts = self._run_suite(code, suite)
            attempts = 0
            while not self._passed(run, counts) and attempts < self.max_fix_attempts:
                attempts += 1
                code = self._ask(
                    TDD_FIX.format(code=code, tests=suite, feedback=feedback(run, counts)),
                    calls,
                )
                run, counts = self._run_suite(code, suite)

            steps.append(
                MethodStep(
                    method=name,
                    tests_in_suite=counts.tests_total,
                    red_passed=red_passed,
                    coded=True,
                    fix_attempts=attempts,
                    green_passed=counts.tests_passed,
                    green=self._passed(run, counts),
                ).model_dump()
            )

        return AgentResult(task_id=task["task_id"], code=code, calls=calls, steps=steps)

    @staticmethod
    def _passed(run: RunOutput, counts: TestCounts) -> bool:
        """Same rule as the grader's class_passed."""
        return counts.tests_total > 0 and counts.tests_passed == counts.tests_total and not run.timed_out