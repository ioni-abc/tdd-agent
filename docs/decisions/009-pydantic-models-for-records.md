# 009: Pydantic models for results that cross a boundary

- **Status:** Accepted
- **Date:** 2026-11-05

## Context

`parse_log` first returned a plain dict. Results will be saved to JSON and read back later (re-grading, reports), and agent output arrives from an LLM: data whose shape can't be trusted. `pydantic` is already a dependency of `anthropic`.

## Decision

Use Pydantic models where data crosses a boundary (disk, LLM), not everywhere:

| Function | Returns | Model? |
| --- | --- | --- |
| `run_tests` | raw log | No: plain `str`, nothing to structure |
| `parse_log` | test counts | Yes: `TestCounts` |
| `grade` | full record | Yes: a record that contains `TestCounts` |
| `load_tasks` | tasks | Not yet: a `Task` model would give typed access and catch key typos, but changes every signature that takes a task. Revisit if dict keys cause bugs |
| agents (later) | code, tests, usage | Yes |

Records are saved with `.model_dump_json()` and loaded with `.model_validate_json()`, so a broken results file fails loudly instead of silently.

## Consequences

- Field names and types of every saved record are defined in one place.
- Models are validated when created; the grader can't produce a record with a missing count.
