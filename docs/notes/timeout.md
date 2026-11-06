# The runner's timeout (`grading/runner.py`)

Generated code can loop forever. Without a timeout, one such task hangs the whole run.

## `RunOutput`

The runner now reports two things, so it returns a small model instead of a bare string:

```python
class RunOutput(BaseModel):
    log: str
    timed_out: bool
```

## The pieces

```python
TIMEOUT_SECONDS = 5  # config.py: per test run, as in the ClassEval paper and the prototype

def run_tests(code: str, test_code: str, timeout: float = config.TIMEOUT_SECONDS) -> RunOutput:
    ...
        try:
            res = subprocess.run([...], capture_output=True, text=True, cwd=tmpwd, timeout=timeout)
            return RunOutput(log=res.stderr, timed_out=False)
        except subprocess.TimeoutExpired as e:
            partial = e.stderr.decode() if isinstance(e.stderr, bytes) else (e.stderr or "")
            return RunOutput(log=partial, timed_out=True)
```

- `timeout: float = config.TIMEOUT_SECONDS`: a default from config; a caller (e.g. the TDD loop) can override it.
- `timeout=timeout` in `subprocess.run`: if the process runs longer, Python **kills it** and raises `subprocess.TimeoutExpired` instead of returning.
- `except subprocess.TimeoutExpired as e`: the run doesn't crash; it returns a result marked `timed_out=True`.
- `e.stderr`: what unittest printed before it was killed. Even with `text=True` this can be **bytes** (a Python quirk), hence `.decode()`; it can also be `None`, hence `or ""`.

## In the grader

```python
class_passed = counts.tests_total > 0 and counts.tests_passed == counts.tests_total and not run.timed_out
```

A class that timed out never counts as passed, even if the tests that finished were green. `timed_out` is stored in `GradeRecord` so the summary can show why a class failed.

## Checkpoint

```bash
uv run python -c "
from tdd_agent.grading.runner import run_tests
r = run_tests('import time', 'import unittest\nclass T(unittest.TestCase):\n    def test_x(self):\n        time.sleep(10)')
print(r.timed_out)
"
```

Prints `True` after about 5 seconds, not 10.

## `grade(task, code, test_code)`

Since this step the grader takes the tests to run as an argument instead of always using `task["test"]`. The same function serves the final grade and, later, the TDD agent's red/green checks on its growing suite. Reference run: `grade(task, task[code_key], task["test"])`.
