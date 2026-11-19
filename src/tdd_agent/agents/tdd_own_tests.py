"""Experiment 2: the TDD agent writes each method's tests itself, then implements the method.

Same loop as TDDAgent; only the tests change. For each method, before the red run,
one extra LLM call writes the tests from the specification (never from the code).
The tests are then fixed: later calls may change the code, not the tests.
"""

from tdd_agent.agents.tdd import TDDAgent
from tdd_agent.grading.parser import parse_log
from tdd_agent.grading.runner import run_tests
from tdd_agent.llm import LLM, LLMCall
from tdd_agent.prompts import TDD_WRITE_TESTS, TEST_WRITER_SYSTEM
from tdd_agent.test_writing import UnusableTests, clean_tests

UNITTEST_HEADER = "import unittest\n"


class TDDOwnTestsAgent(TDDAgent):
    name = "tdd-own"

    def __init__(self, llm: LLM, max_fix_attempts: int = 3, run=run_tests, tests_per_method: int = 5, test_attempts: int = 2):
        super().__init__(llm, max_fix_attempts, run)
        self.tests_per_method = tests_per_method  # option A: about as many as ClassEval has (mostly 5)
        self.test_attempts = test_attempts  # calls allowed to get usable tests for one method

    @property
    def settings(self) -> dict:
        return super().settings | {"tests_per_method": self.tests_per_method, "test_attempts": self.test_attempts}

    def _suite_header(self, task: dict) -> str:
        return UNITTEST_HEADER  # not ClassEval's test imports: those belong to its tests

    def _method_tests(self, task, method, skeleton, suite, calls):
        tests, written = self._write_tests(task, method, skeleton, suite, calls, self.tests_per_method)
        return tests, {"tests_given": 0, "tests_written": written, "tests_valid": bool(tests)}

    def _write_tests(self, task: dict, method: dict, skeleton: str, suite: str, calls: list[LLMCall], n: int, extra: str = "") -> tuple[str, int]:
        """Ask for n tests for this method; returns ("", 0) if no usable tests came back."""
        name = method["method_name"]
        test_class = f"AgentTest_{name}"
        prompt = TDD_WRITE_TESTS.format(
            skeleton=skeleton, suite=suite, n=n, method=name, extra=extra, test_class=test_class, class_name=task["class_name"]
        )
        retry = ""
        for _ in range(self.test_attempts):
            reply = self._ask(prompt + retry, calls, system=TEST_WRITER_SYSTEM)
            try:
                tests, count = clean_tests(reply, test_class, task["class_name"])
                self._check_loads(skeleton, suite + "\n\n" + tests)
                return tests, count
            except UnusableTests as e:
                retry = f"\n\nYour previous tests could not be used: {e}\nWrite them again."
        return "", 0

    def _check_loads(self, skeleton: str, suite: str) -> None:
        """The suite must still load: a bad import or name at module level would break every later run.

        Checked against the skeleton, so it can only judge the tests if the skeleton itself is valid
        Python. Three ClassEval skeletons are not (22, 43, 46: an unclosed docstring, curly quotes);
        there the check is skipped, and the red run's "could not run" feedback lets the LLM repair it.
        """
        try:
            compile(skeleton, "<skeleton>", "exec")
        except SyntaxError:
            return
        run = self.run(skeleton, suite)
        if "_FailedTest" in run.log or parse_log(run.log).tests_total == 0:
            raise UnusableTests("The test file fails to load:\n" + run.log[-1500:])
