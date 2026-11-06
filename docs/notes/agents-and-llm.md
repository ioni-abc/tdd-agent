# Agents and the LLM wrapper

## Dependency injection

**Without it**, the agent decides which LLM it uses:

```python
class BaselineAgent:
    def __init__(self):
        self.llm = LLM()            # always this exact LLM

# or, as in the prototype, the client is built inside the method:
def generate(self, task):
    client = anthropic.Anthropic()
    message = client.messages.create(model="claude-haiku-5-5", ...)
```

**With it**, the agent receives it; the code that starts the run decides:

```python
class BaselineAgent:
    def __init__(self, llm: LLM):
        self.llm = llm

agent = BaselineAgent(llm=LLM())                         # real model
agent = BaselineAgent(llm=LLM(model="claude-opus-5-5"))  # another model, same agent code
agent = BaselineAgent(llm=FakeLLM())                     # a test, no API costs
```

| You want to... | Without DI | With DI |
| --- | --- | --- |
| run the agent on another model | edit the agent | pass another `LLM` |
| give baseline and TDD the same settings | hope both files agree | create one `LLM`, pass it to both |
| test without API calls | impossible | pass a fake with a `call()` method |
| record the model in `run.json` | dig into the agent | `generate.py` made the `LLM`, so it knows |

`LLM(client=None)` is injection one level down: `self.client = client or anthropic.Anthropic()` uses a passed-in client, or creates one.

**DI is not the same as provider-agnostic.** `LLM` uses Anthropic's API (`messages.create`, `message.content`, `message.usage`), so it is model-agnostic within Anthropic only. The *agents* are effectively agnostic: they only call `llm.call(system, user)` and read an `LLMCall`. Another provider would be a second class with the same `call()`.

## `Protocol`

```python
class Agent(Protocol):
    name: str
    def generate(self, task: dict) -> AgentResult: ...
```

- Describes a **shape**: anything with a `name` and a `generate(task)` method is an `Agent`.
- `BaselineAgent` never mentions `Agent`; it fits by having those two things (structural typing, "duck typing").
- Gives: the contract written down in one place, editor warnings when something doesn't fit, no inheritance between agents.
- Not enforced at runtime; a check for editors and type checkers.
- `...` (Ellipsis) means "no body": the protocol describes the method, each agent implements it its own way.

## `interface.py` vs `baseline.py`

| | `interface.py` | `baseline.py` |
| --- | --- | --- |
| What | the contract every agent follows | one agent |
| Contains | `AgentResult`, `Agent` | `BaselineAgent` |
| Does anything? | no, only describes | yes, calls the LLM |

Renamed from `base.py`: "base" (foundation) was too close to "baseline". `tdd.py` will sit next to `baseline.py`; both are strategies for the same contract.

## The baseline agent

```python
def generate(self, task: dict) -> AgentResult:
    user = f"Implement this class:\n\n```python\n{clean_skeleton(task)}\n```"
    call = self.llm.call(CODER_SYSTEM, user)
    return AgentResult(task_id=task["task_id"], code=extract_code(call.reply), calls=[call])
```

- `name = "baseline"` is a class attribute, used for the run folder name.
- The skeleton goes in a ```` ```python ```` block so the model sees where the code starts and ends.
- `calls=[call]`: one call; the TDD agent will put many here.
- `CODER_SYSTEM` lives in `prompts.py`, shared with the TDD agent so the wording is identical.
- `clean_skeleton` (in `dataset.py`): `.strip()` both ends; `skeleton[3:-3]` slices off `ClassEval_5`'s `'''` at each end.

## The temperature removal

`TypeError: Messages.create() got an unexpected keyword argument 'temperature'` came from the SDK, not the code. API version `2026-10-21` (used by `anthropic` 2.x) removed `temperature`, `top_p` and `top_k`; requests sample at temperature 1.0, and Claude 4.7+ models only accept that anyway. So no greedy decoding: every run is sampled (ADR 014). Found by inspecting the installed SDK's `Messages.create` signature, then confirmed in Anthropic's migration guide.

## Bugs from today, and what they teach

| Symptom | Cause | Lesson |
| --- | --- | --- |
| `call()` fails with `AttributeError` on `self.client` | `client = anthropic.Anthropic()` in `__init__` was a local variable | anything a method needs later must be stored on `self` |
| `time.time()` fails | `from datetime import time` imports a class for times of day | `import time` for the module |
| Pydantic rejects `output_tokens=` | field misspelled `ouput_tokens` | Pydantic only accepts declared field names |
| `extract_code(reply)` receives the `LLM` object | defined indented inside the class | a method's first argument is the object; helpers that don't use `self` go at module level |
| `load_dotenv()` at the top of `llm.py` | importing read `.env` | importing does no work; load `.env` in the script that starts a run |
| the model replied "the provided skeleton was just `None`" | `clean_skeleton` had no `return` | a function without `return` returns `None`, and an f-string prints it as the word `None` |
| `grade_run.py: error: unrecognized arguments` | `scripts/grade_run.py` typed twice | argparse counts every word after the script |

## First real runs

3 tasks, `claude-haiku-5-5`: about 7 s per task; 2,881 input and 5,365 output tokens; 2 of 3 classes passed (`ClassEval_0`: 17/19 tests).
