# Saving results (`runs.py`)

## The code, part by part

```python
def reference_dir(label: str) -> Path:
    return config.RESULTS_DIR / "reference" / label
```

Builds the folder from `config.RESULTS_DIR`. `label` is `"benchmark"` or `"skeleton"`, the keys of `REFERENCE_RUNS`.

```python
def save_records(records: list[GradeRecord], run_dir: Path) -> None:
    run_dir.mkdir(parents=True, exist_ok=True)
    for record in records:
        (run_dir / f"{record.task_id}.json").write_text(record.model_dump_json(indent=2), encoding="utf-8")
```

- `mkdir(parents=True, exist_ok=True)`: `parents=True` also creates `results/` and `results/reference/` when missing; `exist_ok=True` means no error when the folder exists, so reruns work.
- `model_dump_json(indent=2)`: Pydantic writes the record, nested `counts` included, as readable JSON.

```python
def load_records(run_dir: Path) -> list[GradeRecord]:
    return [GradeRecord.model_validate_json(p.read_text(encoding="utf-8")) for p in sorted(run_dir.glob("*.json"))]
```

- `model_validate_json`: JSON back into a `GradeRecord`, **checked**: a missing field or wrong type raises instead of giving a broken record.
- `sorted(run_dir.glob("*.json"))`: every JSON file, in a fixed order (unsorted order depends on the file system). Note: sorted by name means `ClassEval_10` comes before `ClassEval_2`.

In `scripts/run_reference.py`, one line per run:

```python
records = run(tasks, code_key)
save_records(records, reference_dir(label))
print_summary(label, records)
```

## Add functions when a step needs them

`load_records` had no caller in A4 except the checkpoint. By the incremental rule (ADR 004) it could wait for D1, its first real caller; it was kept since D1 needs it anyway. The general question to ask of a new function: who calls it, now?

## Reference vs experiments

`runs.py` is **extended, not refactored**, for agent runs (B4): `experiment_dir`, `save_run_info`, `save_code` / `load_code`, `save_calls`. `save_records` is reused unchanged, with `run_dir / "grades"`. See ADR 013.

## Checkpoint

```bash
uv run python scripts/run_reference.py
ls results/reference/benchmark | wc -l      # 100
ls results/reference/skeleton | wc -l       # 100
```

- Pasting several commands at once runs them one after another; their outputs come after the script's.
- `wc -l` on macOS pads the number with spaces (`     100`).
- Anything after `#` on a shell line is a comment.

## Results after the fixes

Benchmark **100/100**, skeleton **0/100**. Two skeleton rows changed compared with the original data, as expected: `ClassEval_31` (19 failed, 2 errored) and `ClassEval_51` (2 failed, 9 errored). Their tests now use `assertAlmostEqual`, which errors rather than fails when the skeleton returns `None` (subtracting from `None` raises a `TypeError`).
