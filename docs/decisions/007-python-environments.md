# 007: Python 3.12 for the project; test interpreter decided by experiment

- **Status:** Accepted: one environment, Python 3.12 (reference run, 2026-11-05)
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

## Outcome (reference run, 2026-11-05)

With the ClassEval test packages installed at compatible versions (decision 010), Python 3.12 reproduces the prototype's 3.8 results:

| | 3.12 (this repo) | 3.8 (prototype) |
| --- | --- | --- |
| Benchmark classes passed | 96/100 | 96/100 |
| Failing benchmark tasks | 17, 31, 48, 51 | 17, 48, 51, 58 |
| Skeleton classes passed | 0/100 | 0/100 |

The only difference caused by Python itself is `ClassEval_31`: Python 3.12's `sum()` uses a more accurate float summation, and the test compares floats exactly (`0.9819805060619655 != 0.9819805060619659`). That is a faulty test, handled under decision 005, not a reason for a second environment. (`ClassEval_58` passing here is covered in decision 006.)

**Therefore:** one environment. No `.venv-eval`, no `EVAL_PYTHON`; `runner.py` keeps `sys.executable`. To state in the thesis: tests were run on Python 3.12 and verified against the 3.8 reference results.

## Consequences

- `runner.py` is the only place that changes between one and two environments.
- A TDD agent that runs tests during generation must use the same interpreter as the final grading, or it can see green during generation and red at grading.
