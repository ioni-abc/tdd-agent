"""Baseline: skeleton in, whole class out, one call (ClassEval's holistic strategy)."""

from tdd_agent.agents.interface import AgentResult
from tdd_agent.dataset import clean_skeleton
from tdd_agent.llm import LLM, extract_code
from tdd_agent.prompts import CODER_SYSTEM


class BaselineAgent:
    name = "baseline"

    def __init__(self, llm: LLM):
        self.llm = llm

    def generate(self, task: dict) -> AgentResult:
        user = f"Implement this class:\n\n```python\n{clean_skeleton(task)}\n```"
        call = self.llm.call(CODER_SYSTEM, user)
        return AgentResult(
            task_id=task["task_id"],
            code=extract_code(call.reply),
            calls=[call],
        )