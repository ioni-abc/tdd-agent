# 013: Results storage in `runs.py`; reference results committed to git

- **Status:** Accepted
- **Date:** 2026-11-06

## Context

The reference runs (benchmark, skeleton) are run once and then cited; the agent runs will be repeated and compared. Both produce `GradeRecord`s that must be saved and read back later (the comparison table should not regrade 100 tasks every time its layout changes).

## Decision

- **Repository pattern:** `src/tdd_agent/runs.py` is the only module that knows the `results/` layout. Other modules ask it to save and load.
- **Now (step A4):**
  - `reference_dir(label)` → `results/reference/<label>/`; the labels are the keys of `REFERENCE_RUNS`, so names line up.
  - `save_records(records, run_dir)` → one `<task_id>.json` per record (`model_dump_json`).
  - `load_records(run_dir)` → `GradeRecord`s back, validated (`model_validate_json`), sorted by file name. First real caller: the comparison table (D1).
- **Later (step B4), by adding functions, not changing these:** `experiment_dir(run_name)`, `save_run_info` (`run.json`), `save_code` / `load_code`, `save_calls`. Grades of an experiment go through the same `save_records`, into `<run>/grades/`.

```
results/
├── reference/{benchmark,skeleton}/<task_id>.json
└── experiments/<run_name>/
    ├── run.json   code/   calls/   grades/
```

- **The reference results are committed to git** (200 small JSON files): they are run once and cited, so they belong in the history. Whether experiment results are committed is decided at B4.

## Consequences

- `save_records` takes the folder as an argument, so it serves reference runs and experiments alike (the same idea as `grade` taking the tests as an argument).
- Changing the folder layout touches one module.
- Reference run on the fixed data, saved: benchmark 100/100, skeleton 0/100.
