# 002: The grader takes code, not a source label

- **Status:** Accepted
- **Date:** 2026-11-05

## Context

In the prototype, `grade_task(task, solution="agent" | "benchmark" | "skeleton", run=...)` decided where the code came from and read agent output from disk. So the grader knew about agents, runs and folders, and an agent could not call it on code it had just written.

## Decision

- `grade(task, code) -> record`: grades whatever code it is given. The caller decides where the code came from.
  - reference runs: `grade(task, task["solution_code"])`, `grade(task, task["skeleton"])`
  - experiments: `grade(task, generated_code)`
- Underneath, `run_tests(code: str, test_code: str) -> str` takes two **strings**, not a task dict, so a TDD agent can run its *own* tests with it.
- Running, parsing and saving are separate: `runner.py` runs, `parse.py` parses, `runs.py` saves. The prototype's `run_and_save` did all three.

## Consequences

- The grader has no knowledge of agents or result folders.
- The same runner serves the final grading and, later, an agent's red/green loop.
