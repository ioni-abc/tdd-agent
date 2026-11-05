# 007: Python 3.12 for the project; test interpreter decided by experiment

- **Status:** Proposed (decided at the first reference run)
- **Date:** 2026-11-05

## Context

- ClassEval's tests were written for Python 3.8, and its `requirements.txt` pins packages that don't install on 3.12 (e.g. `numpy~=1.22`, `pandas~=1.4`).
- The agent libraries need Python ≥ 3.10: `anthropic`, `openai`, `langgraph`, `langchain-core` and `pydantic` all require it (PyPI, Nov 2026). Python 3.8 has had no security updates since October 2024.
- The prototype used two venvs and ran each script by hand in the right one; the grader used `sys.executable`, i.e. whatever Python ran `grade.py`.
- Only the test subprocess needs ClassEval's environment. The grader and agents are ordinary project code.

## Decision

- The project venv (`.venv`) is Python 3.12; all project code runs there.
- `grading/runner.py` starts with `sys.executable` (3.12).
- At the first reference run, all 100 reference solutions are run on 3.12 and compared with the prototype's 3.8 results:
  - **same tasks pass:** one environment; state in the thesis that this was verified.
  - **some newly fail:** either add a 3.8 `.venv-eval` used through a fixed `EVAL_PYTHON` path, or treat those tasks under decision 005.
- Tests always run in a subprocess, whatever the interpreter, for timeouts and isolation.

## Consequences

- `runner.py` is the only place that changes between one and two environments.
- A TDD agent that runs tests during generation must use the same interpreter as the final grading, or it can see green during generation and red at grading.
