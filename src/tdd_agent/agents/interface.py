from typing import Protocol
from pydantic import BaseModel
from tdd_agent.llm import LLMCall

class AgentResult(BaseModel):
    task_id: str
    code: str
    calls: list[LLMCall]
    steps: list[dict] = []  # agent-specific step log (e.g. the TDD agent's red/green per method)
    tests: str = ""  # the test suite the agent built and ran (TDD agents), saved to tests/<task_id>.py


class Agent(Protocol):
    name: str

    def generate(self, task: dict) -> AgentResult: ...