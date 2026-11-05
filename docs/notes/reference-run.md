# The reference run (`scripts/run_reference.py`)

Grades ClassEval's reference solutions ("benchmark") and empty skeletons for all 100 tasks. Run once:

```bash
uv run python scripts/run_reference.py   # from the project root
```

## Results (2026-11-05, Python 3.12)

| | Classes passed | Failing |
| --- | --- | --- |
| Benchmark | 96/100 | 17, 31, 48, 51 |
| Skeleton | 0/100 | all |

Matches the prototype on 3.8 (96/100, failing 17, 48, 51, 58) apart from 31 and 58. See ADR 006 and ADR 007.

## How the benchmark went from 15 failures to 4

| Run | Failing | What was wrong |
| --- | --- | --- |
| 1 | 15 | 12 tasks couldn't import their packages (none installed in the project venv) |
| 2 | 5 | packages installed at latest versions: 51 broke on NumPy 2 (`np.mat` removed), 69 lacked `reportlab` |
| 3 | 4 | `numpy<2`, `pandas<3`, `reportlab` (ADR 010) |

## Reading the output

| Pattern | Meaning |
| --- | --- |
| `0/1 (0 failed, 1 errored)` | The test file **couldn't be imported** (e.g. missing package). unittest reports one fake "test" that errored. |
| `0/0 (0 failed, 0 errored)` | unittest **crashed before running anything**, e.g. a `SyntaxError` in the code (`ClassEval_22`'s skeleton has an unterminated docstring). No `Ran N tests` line, no headers, so everything is 0. Correctly not passed thanks to `tests_total > 0`. |
| `0/26 (0 failed, 26 errored)` | Every test **crashed** rather than failing an assertion, e.g. a skeleton method returns `None` and the test calls a method on it. |
| `28/29 (1 failed, 0 errored)` | One assertion false. |

**Print `passed/total`, not `passed/failed`.** The first version printed `tests_passed/tests_failed`, which made `9/2` and `11/10` look broken. And without the errored count, crashed tasks showed as a misleading `0/0`.

Later: add the process's return code to the record, so "crashed" can be told apart from "ran zero tests".

## Why the script was rewritten

First version: one `run()` that graded **and** printed in the same loop, kept a counter next to a list holding the same information, read a module-level `tasks`, and called `run()` at import.

| Change | Why |
| --- | --- |
| Drop the counter; use `len(failed)` | Two variables that must stay in sync are a bug waiting to happen |
| List comprehensions: `[grade(t, t[key]) for t in tasks]`, `[r for r in records if not r.class_passed]` | Each line reads as one sentence |
| `run()` returns records; `print_summary()` prints | Functional core / imperative shell; step 7 needs the records to **save** them |
| `REFERENCE_RUNS = {"benchmark": "solution_code", "skeleton": "skeleton"}` | The label-to-key pairing is data; written once, looped over, and reused as folder names in step 7 |
| `r.task_id` instead of `task["task_id"]` | The record carries it; the printing function doesn't have the task |
| Report `96/100 classes passed` | The positive number is the one cited |
| `main()` + `if __name__ == "__main__":` | Runs only when executed, not on import |

```python
def main() -> None:
    tasks = load_tasks()
    for label, code_key in REFERENCE_RUNS.items():
        records = run(tasks, code_key)
        print_summary(label, records)
```
