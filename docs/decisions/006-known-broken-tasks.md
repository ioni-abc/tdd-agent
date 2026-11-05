# 006: Exclude known-broken tasks from main results

- **Status:** Accepted (carried over from the prototype)
- **Date:** 2026-11-05

## Context

In the prototype, some tasks failed even with ClassEval's own reference solution:

| Task | Why it fails with the reference solution |
| --- | --- |
| `ClassEval_17` | date-dependent |
| `ClassEval_48` | hostname-dependent |
| `ClassEval_51` | floating-point precision |
| `ClassEval_58` | added to `KNOWN_BROKEN` later in the prototype; reason to be filled in |

The prototype also found that about 7% of tests (157 of ~2,200) pass with the empty skeleton, while no skeleton passes a full class.

## Decision

- `KNOWN_BROKEN` lives in `dataset.py`.
- These tasks are excluded from the main results, and the exclusion is reported with its reasons.
- Test-level pass rates are always reported next to the skeleton baseline; class-level pass rate is the primary metric.
- The list is re-checked by the reference run in this repo; under decision 005 these tasks are candidates for fixing rather than exclusion.

## Consequences

- Summaries show results with and without the known-broken tasks.
