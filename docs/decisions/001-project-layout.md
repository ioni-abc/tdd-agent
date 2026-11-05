# 001: One uv package, one module per job

- **Status:** Accepted
- **Date:** 2026-11-05

## Context

The prototype had two scripts, `grade.py` and `generate_tdd.py`, each mixing several jobs: paths, loading data, running tests, parsing output, choosing where code comes from, calling the LLM, the agent's workflow, saving files, and the CLI. Paths were defined twice, differently (`.parent` vs `.parent.parent`). The grader could not be reused by an agent.

The reference runs (benchmark and skeleton) run once; the agents are where experiments happen. Both need the grader.

## Decision

A single uv package with the `src/` layout, split into modules that each do one job:

```
src/tdd_agent/
├── config.py        # paths and fixed settings
├── dataset.py       # load_tasks(), clean_skeleton(), KNOWN_BROKEN
├── grading/
│   ├── runner.py    # run_tests(code, test_code) -> raw log
│   ├── parse.py     # parse_log(log) -> counts + failure reasons
│   └── grade.py     # grade(task, code) -> record
├── llm.py           # call(), extract_code()
├── agents/          # one file per agent
└── runs.py          # run names, run folders, saving

scripts/
├── run_reference.py # once: benchmark + skeleton
├── generate.py      # run an agent over tasks
└── grade_run.py     # grade one experiment run
```

Dependencies point one way: `scripts/` → `agents/`, `grading/`, `runs.py`; `agents/` → `llm.py`, `dataset.py`, `grading/runner.py`; `grading/` → `dataset.py`, `config.py`. Nothing imports from `scripts/`, and `grading/` never imports from `agents/`.

Results keep the one-off reference runs apart from experiments, and everything about one run in one folder:

```
results/
├── reference/{benchmark,skeleton}/<task_id>.json
└── experiments/<run_name>/
    ├── run.json      # agent, model, prompt version, date
    ├── code/  tests/  calls/  grades/
```

## Consequences

- Only `config.py` builds paths; every other module imports them.
- Importing a module does no work: no file reads or printing at module level.
- Re-grading an old run, or deleting one, touches a single folder.
