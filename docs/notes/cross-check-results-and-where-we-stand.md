# Cross-check results, and where the thesis stands (27 Nov 2026)

## What the cross-check is
- Every test of `task["test"]` (2196) has a label in `results/analysis/benchmark_labels.csv`, made by `scripts/label_tests.py` with `claude-haiku-5-5` (judge prompt after commit `06939cd`): `stated`, `unstated`, `contradicts`, `other_inconsistency`, or `no_method_info` (108 class-level tests, not judged).
- `scripts/rescore_stated.py` joins each run's per-test results (`results/experiments/<run>/grades/ClassEval_<n>.json`, field `log`) with those labels on the key `(task_id, test class, test name)` and counts passed/total per label.
- One labeling only. Output: `results/analysis/rescore_stated.csv`.

## Results

Agents: no-tests-agent = baseline (`baseline_2026-11-19T14-38-59`), bm-tests-agent = TDD agent v1 (`tdd_2026-11-19T14-38-58`), own-tests-agent = `tdd-own` (`tdd-own_2026-11-19T14-38-57`).

| Label (tests) | no-tests-agent | bm-tests-agent | own-tests-agent |
| --- | --- | --- | --- |
| `stated` (1572) | 1527 (97.1%) | 1559 (99.2%) | 1523 (96.9%) |
| `unstated` (414) | 307 (74.2%) | 407 (98.3%) | 286 (69.1%) |
| `contradicts` (44) | 15 (34.1%) | 44 (100.0%) | 13 (29.5%) |
| `other_inconsistency` (58) | 55 (94.8%) | 58 (100.0%) | 54 (93.1%) |
| `no_method_info` (108) | 86 (79.6%) | 100 (92.6%) | 78 (72.2%) |
| Classes passing all tests, as graded | 51/100 | 97/100 | 43/100 |
| Classes passing all their `stated` tests | 86/99 | 98/99 | 84/99 |

99, not 100: ClassEval_69 has no `stated` test.

## What the numbers support
- On `stated` tests the three agents are within about 2 points (96.9% to 99.2%).
- Most of the headline gap is in `unstated` and `contradicts` tests: the gap in classes falls from 54 (97 vs 43) to 14 (98 vs 84) when only `stated` tests count.
- The bm-tests-agent passes all 44 `contradicts` tests: given tests, it satisfies them even where the docstring says otherwise. It was never told the tests could be wrong.

## What they do not support
- That writing its own tests helps: own-tests-agent is at or below the baseline in every row.
- That bm-tests-agent is better at implementing from a spec: it sees the tests it is graded on.
- Any claim with error bars: one sampled run per agent, 100 tasks, labels from one cheap LLM judge, not checked by hand. `contradicts` is 44 tests.

## Where we stand (Ivan's concern)
- Most of the time went into finding and working around defects of ClassEval: 5 broken tasks, skeleton defects (ClassEval_25, 49), the docstring/test mismatch, labeling and re-scoring. Little time went into an experiment that yields knowledge about agents.
- The professor's question for the thesis: how is it relevant and interesting to the reader, and what knowledge did it produce?
- Without the benchmark work, the remaining agent work is not at the level of a semester thesis.
- "Agents need supervision; wrong input gives wrong output" is not a useful finding: anyone could say it without a thesis.
- There is no decisive experiment yet that supports a thesis claim.

## Open questions for the professor
- Which research question the thesis should answer, given what the benchmark work showed.
- Whether the benchmark work (the per-test labels and the re-score as graded vs on `stated` tests) can be a contribution in its own right.
- What experiment, within the time left (submission before 23 Dec 2026), would give a decisive result.
