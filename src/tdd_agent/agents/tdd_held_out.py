"""Held-out experiment: the TDD agent v1 loop, but each method gets only its shown tests.

The split (which of a method's ClassEval tests are shown, which hidden) comes from
data/held_out_split.json, written by scripts/make_split.py. The agent never sees the hidden
tests; scripts/rescore_held_out.py grades every run on them, so this agent, the baseline and
tdd-own are all scored on tests none of them has seen.
"""

import json

from tdd_agent import config
from tdd_agent.agents.tdd import TDDAgent
from tdd_agent.dataset import select_tests, tests_for_method
from tdd_agent.grading.runner import run_tests
from tdd_agent.llm import LLM


def load_split(path=config.HELD_OUT_SPLIT_PATH) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"{path} is missing: run scripts/make_split.py first")
    return json.loads(path.read_text(encoding="utf-8"))


class TDDHeldOutAgent(TDDAgent):
    name = "tdd-heldout"

    def __init__(self, llm: LLM, max_fix_attempts: int = 3, run=run_tests, split: dict | None = None):
        super().__init__(llm, max_fix_attempts, run)
        self.split = split or load_split()

    @property
    def settings(self) -> dict:
        return super().settings | {"shown_per_method": self.split["shown_per_method"], "seed": self.split["seed"]}

    def _method_tests(self, task, method, skeleton, suite, calls):
        shown = self.split["tasks"][task["task_id"]][method["method_name"]]["shown"]
        tests = select_tests(tests_for_method(task, method), set(shown))
        return tests, {"tests_given": len(shown)}
