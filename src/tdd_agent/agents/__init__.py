"""The interface every agent implements (Strategy pattern, ADR 003)."""

from typing import Protocol

from pydantic import BaseModel

from tdd_agent.llm import LLMCall


class AgentResult(BaseModel):
    task_id: str
    code: str
    calls: list[LLMCall]


class Agent(Protocol):
    name: str

    def generate(self, task: dict) -> AgentResult: ...