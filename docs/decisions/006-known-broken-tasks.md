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

## Re-check in this repo (reference run, 2026-11-05, Python 3.12)

| Task | Result with the reference solution | Status |
| --- | --- | --- |
| `ClassEval_17` | 28/29 | still broken: date-dependent |
| `ClassEval_31` | 20/21 | **new**: exact float comparison vs Python 3.12's more accurate `sum()` (`0.9819805060619655 != 0.9819805060619659`); candidate for fixing under 005 |
| `ClassEval_48` | 15/16 | still broken: hostname-dependent |
| `ClassEval_51` | 8/11 | still broken: floating-point precision (with `numpy<2`; with NumPy 2 it errors on the removed `np.mat`) |
| `ClassEval_58` | passes | **no longer broken** here; why the prototype listed it is still to be checked |

Proposed `KNOWN_BROKEN` for this repo: `{17, 31, 48, 51}`, pending the test-fix audit (005), which may move 31 and 51 to the fixed set.

## Consequences

- Summaries show results with and without the known-broken tasks.
