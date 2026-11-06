import re
import time

import anthropic
from pydantic import BaseModel

from tdd_agent import config

CODE_BLOCK = re.compile(r"```(?:python)?\n(.*?)```", re.DOTALL)

class LLMCall(BaseModel):
    model: str
    stop_reason: str | None
    input_tokens: int
    output_tokens: int
    seconds: float
    reply: str


class LLM:
    # dependency injection
    def __init__(self, client=None, model=config.MODEL, max_tokens=config.MAX_TOKENS):
        self.client = client or anthropic.Anthropic()
        self.model = model
        self.max_tokens = max_tokens


    def call(self, system: str, user: str) -> LLMCall:
        start = time.time()
        message = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        reply = "".join(block.text for block in message.content if block.type == "text")
        return LLMCall(
            model=message.model,
            stop_reason=message.stop_reason,
            input_tokens=message.usage.input_tokens,
            output_tokens=message.usage.output_tokens,
            seconds=round(time.time() - start, 1),
            reply=reply
        )

def extract_code(reply):
    blocks = CODE_BLOCK.findall(reply)
    if not blocks:
        return reply.strip()
    return max(blocks, key=len).strip()
