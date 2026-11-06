# 015: An LLM wrapper injected into agents; one agent interface; shared prompts

- **Status:** Accepted
- **Date:** 2026-11-06

## Context

The prototype created the API client inside each agent script and kept the prompts inside the agent files. A second agent (TDD) is coming that must use the same model, settings and coder prompt as the baseline.

## Decision

- **`llm.py`:** `class LLM` holds the client and settings (`config.MODEL`, `config.MAX_TOKENS`); `call(system, user) -> LLMCall` returns the reply with model, stop reason, tokens and seconds. `extract_code()` and its `CODE_BLOCK` regex live next to it (a constant goes where it is used, unless it is a setting).
- **Dependency injection, at two levels:** `LLM(client=None)` receives its client (a fake client for tests); agents receive an `LLM` (`BaselineAgent(llm)`). The script that starts a run (`generate.py`) decides the model, and records it in `run.json`.
- **`agents/interface.py`** (renamed from `base.py`, to avoid confusion with `baseline.py`): `AgentResult(task_id, code, calls)` and the `Agent` `Protocol` (`name`, `generate(task) -> AgentResult`). Agents fit the shape without inheriting from it (structural typing).
- **`prompts.py`:** the coder system prompt (`CODER_SYSTEM`, the prototype's `CODER_PROMPT`) in one shared place, so both agents use identical wording.
- **`report.py`:** `print_summary` moved out of `run_reference.py`, so scripts don't import from each other.
- **`scripts/generate.py`:** an agent registry, `AGENTS = {"baseline": BaselineAgent}`, chosen on the command line; saves `run.json`, `code/`, `calls/`. **`scripts/grade_run.py`:** grades a saved run into `grades/`.
- `load_dotenv()` is called in `generate.py`, not at module level in `llm.py`.

## Consequences

- The `LLM` class is model-agnostic within Anthropic, not provider-agnostic; the agents are effectively agnostic, since they only use `llm.call(...)`. Another provider would be a second class with the same `call()`.
- Adding the TDD agent is one new file plus one registry line.
- The whole generate → save → grade path was tested with a fake client before any API call.
