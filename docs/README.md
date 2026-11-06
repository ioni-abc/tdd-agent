# Docs

Two kinds of documents live here, both in Markdown and versioned with the code.

| Folder | What goes in it | Written when |
| --- | --- | --- |
| `notes/` | Learning notes: something I didn't know and now understand. Question, answer, small example. | Right after the question comes up |
| `decisions/` | Architecture Decision Records (ADRs): a design choice, why it was made, and what follows from it. | When a decision is made, or when it changes |

Notes are for me. Decisions feed the design chapter of the thesis.

| Note | Covers |
| --- | --- |
| [python.md](notes/python.md) | paths, imports, lambda, temp files, subprocess |
| [tooling.md](notes/tooling.md) | uv (incl. dependency groups and conflicts), Ruff, venvs, VS Code, macOS, git and GitHub |
| [evaluation.md](notes/evaluation.md) | decoding, pass@k, ClassEval strategies, TGen |
| [parsing-unittest-logs.md](notes/parsing-unittest-logs.md) | `parse_log` line by line, regex reference |
| [grader.md](notes/grader.md) | `grade()` and `GradeRecord`, Pydantic basics, review notes |
| [reference-run.md](notes/reference-run.md) | the reference run: results, reading the output, the script's refactor |
| [timeout.md](notes/timeout.md) | the runner's timeout, `RunOutput`, `TimeoutExpired` |
| [classeval-tests.md](notes/classeval-tests.md) | how ClassEval's tests are organised; the visible/hidden split, explained |
| [benchmark-fixes.md](notes/benchmark-fixes.md) | how the five broken tasks were diagnosed and fixed; flaky tests; fixes as data |
| [saving-results.md](notes/saving-results.md) | `runs.py` part by part, reference vs experiment layout, the checkpoint |

## Decision records

- One file per decision: `NNN-short-title.md`, numbered in order and never renumbered.
- Each has a **Status**: `Proposed` (suggested, not yet confirmed), `Accepted`, or `Superseded by NNN`.
- A decision that changes is not edited away: mark it `Superseded` and write a new record.

| # | Decision | Status |
| --- | --- | --- |
| [001](decisions/001-project-layout.md) | One uv package, one module per job | Accepted |
| [002](decisions/002-grader-takes-code.md) | The grader takes code, not a source label | Accepted |
| [003](decisions/003-design-patterns.md) | Design patterns used, and those avoided | Accepted |
| [004](decisions/004-incremental-development.md) | Build module by module, simplest version first | Accepted |
| [005](decisions/005-classeval-data-and-test-fixes.md) | Pin ClassEval data; fix broken tests (or reference solutions) in a separate, logged copy: 5 fixed, 100/100 | Accepted |
| [006](decisions/006-known-broken-tasks.md) | Exclude known-broken tasks from main results | Superseded by 005's fixes: nothing excluded |
| [007](decisions/007-python-environments.md) | One environment, Python 3.12 (verified against the 3.8 results) | Accepted |
| [008](decisions/008-evaluation-metric.md) | Greedy class-level pass@1 as the main metric (pass@3 parked) | Proposed |
| [009](decisions/009-pydantic-models-for-records.md) | Pydantic models for results that cross a boundary | Accepted |
| [010](decisions/010-eval-dependency-group.md) | ClassEval's test packages in an `eval` group, pinned (`numpy<2`, `pandas<3`) | Accepted |
| [011](decisions/011-tdd-agent-v1-sees-all-tests.md) | TDD agent v1 receives all of ClassEval's tests, method by method; split later | Accepted |
| [012](decisions/012-tdd-agent-loop.md) | The TDD agent's red/green loop | Proposed |
| [013](decisions/013-results-storage.md) | Results storage in `runs.py`; reference results committed to git | Accepted |

## Commit messages

Commits that only touch `docs/` use a prefix, so they stand apart from code commits in the history:

- `docs(notes): …` for learning notes
- `docs(adr): …` for decision records
- `docs: …` for anything else in `docs/`

Code commits keep the `Add: …` style.

## Plan

The step-by-step to-do list for the 13 Nov meeting: [Thesis to-do: TDD agent for the 13 Nov meeting](https://claude.ai/artifact/Uda2wxkCkqknWKkY1HiN7n).
