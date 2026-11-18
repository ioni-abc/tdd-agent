"""Experiment 3: the TDD agent receives some of each method's ClassEval tests and writes the rest.

For a method with n ClassEval tests, it receives the first ceil(given_ratio * n) and writes
n minus that many more itself, after seeing the given ones. The ClassEval tests it never sees
are still in the final grading, so the grade shows how far its own tests got it.
A method without ClassEval tests gets tests_per_method written tests, as in experiment 2.
"""

from tdd_agent.agents.tdd import TDDAgent
from tdd_agent.agents.tdd_own_tests import TDDOwnTestsAgent
from tdd_agent.dataset import split_method_tests, test_header, tests_for_method
from tdd_agent.grading.runner import run_tests
from tdd_agent.llm import LLM

EXTRA = """The suite already has {given} given tests for `{method}` (class {given_class}).
Write tests for behaviour they don't cover, without repeating them."""


class TDDMixedTestsAgent(TDDOwnTestsAgent):
    name = "tdd-mixed"

    def __init__(self, llm: LLM, max_fix_attempts: int = 3, run=run_tests, tests_per_method: int = 5, test_attempts: int = 2, given_ratio: float = 0.6):
        super().__init__(llm, max_fix_attempts, run, tests_per_method, test_attempts)
        self.given_ratio = given_ratio  # 0.6: of ClassEval's usual 5 tests, 3 given and 2 written

    @property
    def settings(self) -> dict:
        return super().settings | {"given_ratio": self.given_ratio}

    def _suite_header(self, task: dict) -> str:
        return TDDAgent._suite_header(self, task)  # ClassEval's imports: the given tests need them

    def _method_tests(self, task, method, skeleton, suite, calls):
        given, given_count, total = split_method_tests(tests_for_method(task, method), self.given_ratio)
        to_write = total - given_count if total else self.tests_per_method
        written, written_count = "", 0
        if to_write > 0:
            extra = EXTRA.format(given=given_count, method=method["method_name"], given_class=method["test_class"]) if given else ""
            base = suite + "\n\n" + given if given else suite
            written, written_count = self._write_tests(task, method, skeleton, base, calls, to_write, extra)
        tests = "\n\n".join(part for part in (given, written) if part)
        origin = {"tests_given": given_count, "tests_written": written_count, "tests_valid": to_write == 0 or bool(written)}
        return tests, origin
