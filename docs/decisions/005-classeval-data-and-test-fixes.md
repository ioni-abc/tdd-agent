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

## Consequences

- Results stay comparable with the paper (original tests) while the corrected set removes noise.
