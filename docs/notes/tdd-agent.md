# The TDD agent (`agents/tdd.py`)

Design decision: ADR 012. This note walks through the code.

## The helpers it builds on (`dataset.py`)

```python
def test_header(task) -> str:          # the imports before the first "class" in task["test"]
def tests_for_method(task, method):    # the seam for a later split: today the method's full test class
def methods_in_order(task):            # each method after the methods it calls
```

- **`test_header`:** the per-method test copies start with `class ...` and have no imports. In all 100 tasks the part before the first class is imports only.
- **`tests_for_method`:** the only place the agent gets tests from. A visible/hidden split (ADR 011) would change only this function.
- **`methods_in_order`:**

  ```python
  ready = next(
      (m for m in remaining if set(m["dependencies"]["method_dependencies"]) <= done),
      remaining[0],  # cycle: take the first left
  )
  ```

  `set(...) <= done` is "every dependency is already done" (subset). `next(generator, default)` returns the first match, or the default when there is none, which only happens in a cycle.

## The loop, part by part

```python
code = clean_skeleton(task)
suite = test_header(task)
for method in methods_in_order(task):
    suite += "\n\n" + tests_for_method(task, method)
    run, counts = self._run_suite(code, suite)          # RED
    if self._passed(run, counts):                       # already green
        steps.append(MethodStep(..., coded=False, ...))
        continue
    code = self._ask(TDD_IMPLEMENT.format(...), calls)  # CODE
    run, counts = self._run_suite(code, suite)          # GREEN
    attempts = 0
    while not self._passed(run, counts) and attempts < self.max_fix_attempts:
        attempts += 1
        code = self._ask(TDD_FIX.format(...), calls)    # FIX
        run, counts = self._run_suite(code, suite)
    steps.append(MethodStep(...).model_dump())
```

- **`suite` only grows:** each method's tests are added and never removed, so every green check also re-runs the earlier methods' tests (regression).
- **`continue`** skips the rest of the loop body for this method: no failing test, no new code.
- **`_ask`** makes one call with `CODER_SYSTEM` (the baseline's system prompt), appends the `LLMCall` to `calls`, and returns the extracted code.
- **`_passed`** is the grader's `class_passed` rule: tests ran, all passed, no timeout. A `@staticmethod` because it uses nothing from `self`.
- **`self.run`** is the injected test runner (default `run_tests`), like the injected `LLM`.

## What the model sees

`TDD_IMPLEMENT`: the current code, "implement the method `X` so that all of these tests pass; tests of earlier methods must keep passing", the whole suite, and the red result. `TDD_FIX`: the current code, the suite, and the failures. Both ask for the complete updated class.

`feedback(run, counts)`:

| Situation | What is sent |
| --- | --- |
| timed out | "The tests timed out (possible infinite loop or very slow code)." |
| no test ran (e.g. `SyntaxError`) | "The tests could not run:" + the end of the log |
| all pass | "N of N tests pass." |
| some fail | "X of N tests pass." + the failure blocks, capped at 4,000 characters |

`SEPARATOR + SEPARATOR.join(log.split(SEPARATOR)[1:])`: split the log at unittest's `=====` lines, drop the part before the first failure (the per-test `... ok` lines), and glue the failure blocks back together.

## The step log

`steps/<task_id>.json`, one entry per method:

```json
{"method": "is_start_with", "tests_in_suite": 5, "red_passed": 3, "coded": true,
 "fix_attempts": 1, "green_passed": 5, "green": true}
```

`red_passed` = tests already passing before any code (the empty skeleton passes some); `coded: false` = already green, no call made.

Saved through a new field on the shared result: `AgentResult.steps: list[dict] = []`. The default keeps the baseline unchanged; `runs.save_result` writes `steps/` only when there are steps.

## How it was tested before any API call

A fake client (dependency injection again) whose first reply per method returns the skeleton unchanged (so green fails) and whose fix reply returns the reference solution. That exercises red, code, a failing green, a fix, and a passing green, then `generate.py` saving and `grade_run.py` grading: 2/2 classes passed, and the step log showed `coded: false` for methods already green after the first fix.

## Cost to expect

Per task: one implement call per method that isn't already green, plus up to 3 fix calls each; often only the first method needs code, because the model writes more than asked. Every call carries the current code and the whole suite, so calls get longer as the class grows.

## Git: first push of a new branch

`fatal: The current branch agent has no upstream branch` on the first `git push` of a new branch is normal: git doesn't know which GitHub branch it belongs to yet. `git push -u origin agent` links them; after that, plain `git push`/`git pull` work. `git config --global push.autoSetupRemote true` does this automatically for every new branch.
