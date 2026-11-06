# 005: Pin the ClassEval data; fix faulty tests in a separate, logged copy

- **Status:** Accepted
- **Date:** 2026-11-05

## Context

ClassEval is the problem source. Its public code (commit `eaeac44`, 24 Oct 2024) is more than a year newer than the paper (arXiv v2, Aug 2023). The professor said it's acceptable to change failing, known-error or ambiguous tests in the benchmark (Nov 2026). Changing tests can look like tuning the benchmark to the system, so it needs rules.

## Decision

- `data/ClassEval_data.json` is downloaded from commit `eaeac44` and **never edited**:
  `https://raw.githubusercontent.com/FudanSELab/ClassEval/eaeac44d0d5dcd8a95feec50726d66fedc73a98f/data/ClassEval_data.json`
- Corrections go in a separate file (e.g. `data/ClassEval_data_fixed.json`).
- A test may be fixed only if it is wrong on its own terms: it fails against ClassEval's reference solution, contradicts the docstring, or is ambiguous. Never because an agent fails it.
- Every change is logged: task ID, what was wrong, before/after diff.
- Results are reported on both the original and the corrected tests, and every agent runs on the corrected set too.
- The test audit happens before the experiments.

## Fixes applied (2026-11-06)

The four tasks that fail with their own reference solution (decision 006) are fixed. The professor was in favour of fixing them rather than only excluding them. The fixes live as data in `data/test_fixes.json` (task, test, reason, fix, exact old and new text, expected count) and are applied by `scripts/fix_benchmark.py`, which writes `data/ClassEval_data_fixed.json`.

| Task | Test | What was wrong | Fix |
| --- | --- | --- | --- |
| 17 | `test_get_upcoming_events_5` | time bomb: the "upcoming" event is dated 2 Jan 2024, in the past by now | event moved to 2124 |
| 48 | `test_get_hostname_3` | machine-dependent: expects the test author's laptop name `LAPTOP-2CS86KUM` | `socket.gethostbyaddr` mocked in that test |
| 31 | `test_correlation_coefficient_4` | exact float comparison; Python 3.12's `sum()` changes the last digits | `assertEqual` → `assertAlmostEqual` |
| 51 | `fleiss_kappa` assertions (6) | exact float comparison of NumPy results | `assertEqual` → `assertAlmostEqual` |

Rules the script enforces:

- Each fix states how often its old text occurs; the script stops if the count differs, so a fix never silently changes nothing or the wrong thing.
- Each fix is applied to `task["test"]` **and** to the per-method copies in `methods_info[i]["test_code"]`, so the TDD agent (per-method tests) and the final grade (full suite) see the same tests.
- Only these four tasks differ between the original and the fixed file.

`load_tasks(fixed=True)` is the default; `load_tasks(fixed=False)` loads the original.

## Consequences

- Results stay comparable with the paper (original tests) while the corrected set removes noise.
