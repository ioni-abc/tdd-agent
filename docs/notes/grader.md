# The grader (`grading/grader.py`)

## What it does

The glue between the two halves built before it:

- `run_tests(code, test_code)` **runs** tests and returns the raw log
- `parse_log(log)` **reads** a log and returns `TestCounts`

`grade(task, code)` is the one function the rest of the project calls: "here's a task and some code, how did it do?"

```
task + code
   │
   ├─ 1. run_tests(code, task["test"])   →  log (a long string)
   ├─ 2. parse_log(log)                  →  TestCounts
   └─ 3. pack everything into one GradeRecord
```

The grader doesn't care where the code came from (ADR 002):

```python
grade(task, task["solution_code"])   # reference run
grade(task, task["skeleton"])        # skeleton baseline
grade(task, code_the_agent_wrote)    # experiments
```

## `GradeRecord`

| Field | Value | Why |
| --- | --- | --- |
| `task_id` | `task["task_id"]` | counts alone don't say which task they belong to |
| `counts` | `TestCounts` from `parse_log` | test-level numbers; a model inside a model |
| `class_passed` | every test passed | the main metric |
| `log` | the raw log | to read *why* something failed later |

**The trap in `class_passed`:** if the code crashes before any test runs, `tests_total` and `tests_passed` are both 0, and `0 == 0` is `True`. Hence:

```python
class_passed = counts.tests_total > 0 and counts.tests_passed == counts.tests_total
```

## Checkpoint (`ClassEval_0`)

```
reference solution: 19 / 19  class_passed=True
empty skeleton:      6 / 19  class_passed=False
```

## Pydantic basics (from `TestCounts` and `GradeRecord`)

```python
class TestCounts(BaseModel):
    tests_total: int
    tests_passed: int
```

- `BaseModel`: the parent class every model inherits; gives validation, `.model_dump()`, JSON methods.
- No `__init__`: Pydantic generates it from the fields.
- Each `name: type` line is a field, and the type is **enforced** at creation: `"19"` becomes `19`; `"abc"` or a missing field raises `ValidationError`.
- Created with keyword arguments only: `TestCounts(tests_total=19, ...)`.
- Attribute access: `counts.tests_passed`, not `counts["tests_passed"]`.
- `.model_dump()` → dict; `.model_dump_json()` → JSON string; `Model.model_validate_json(text)` → back, with checking.
- `print(record)` shows **every** field, including the whole log. Print the fields you need instead.

## Review notes

- **`True if cond else False` is redundant:** a comparison already is a `bool`, and `and` between two comparisons gives `True`/`False`.
- **Name things by what they mean to *this* function:** `log`, not `stderr`. That unittest writes to stderr is a detail of `runner.py`.
- **One import style:** absolute imports (`from tdd_agent.grading.parser import ...`) everywhere; Ruff groups and sorts them.
- **No loose strings at module level:** a `"""..."""` block at the bottom of a module is a real value created on every import, just unused. Commands go in notes.
- **Declare what you import directly:** `parser.py` imports `pydantic`, so `uv add pydantic`, even though `anthropic` would pull it in later. Otherwise the grader breaks the day `anthropic` changes its requirement.
