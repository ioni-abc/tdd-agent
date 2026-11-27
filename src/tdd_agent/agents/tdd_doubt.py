"""TDD agent v1 that may doubt its tests (experiment 4).

Same loop and same given tests as TDDAgent. For each method, before the red run, one extra call
shows the agent the method's docstring and tests (the doubt check of scripts/doubt_check.py).
Tests it labels CONTRADICTS are collected, and every later code-writing call gets a note: follow
the docstring where it disagrees with a flagged test, and do not force that test green.
The flagged tests stay in the suite, so the grade still counts them.
"""

from tdd_agent.agents.tdd import TDDAgent
from tdd_agent.dataset import tests_for_method
from tdd_agent.doubt import parse_reply, test_names
from tdd_agent.grading.runner import run_tests
from tdd_agent.llm import LLM, LLMCall
from tdd_agent.prompts import CODER_SYSTEM, DOUBT_CHECK, DOUBT_NOTE, DOUBT_SYSTEM


class TDDDoubtAgent(TDDAgent):
    name = "tdd-doubt"

    def __init__(self, llm: LLM, max_fix_attempts: int = 3, run=run_tests):
        super().__init__(llm, max_fix_attempts, run)
        self._flagged: list[str] = []  # "- test (method): reason", for the task being generated

    def generate(self, task: dict):
        self._flagged = []
        return super().generate(task)

    def _method_tests(self, task, method, skeleton, suite, calls: list[LLMCall]):
        tests = tests_for_method(task, method)
        flagged = []
        if tests.strip():
            call = self.llm.call(DOUBT_SYSTEM, DOUBT_CHECK.format(docstring=method["method_description"], tests=tests))
            calls.append(call)
            answer = parse_reply(call.reply)
            for t in test_names(tests):
                flag, reason = answer.get(t, ("UNPARSED", ""))
                if flag == "CONTRADICTS":
                    flagged.append(t)
                    self._flagged.append(f"- {t} ({method['method_name']}): {reason}")
        return tests, {"doubt_flagged": flagged}

    def _ask(self, prompt: str, calls: list[LLMCall], system: str = CODER_SYSTEM) -> str:
        if self._flagged and system == CODER_SYSTEM:
            prompt += DOUBT_NOTE.format(items="\n".join(self._flagged))
        return super()._ask(prompt, calls, system)
