# Baseline and TDD agent v1 on the fixed benchmark

All experiments were rerun cleanly on the fixed benchmark (`data/ClassEval_data_fixed.json`, see `benchmark-fixes.md`), with the original skeleton kept as a fixed specification in every TDD prompt. Model `claude-haiku-5-5`, one sampled run per approach (ADR 014).

The earlier runs (baseline 48/100; TDD v1 96/100, before the skeleton fix) are kept in the tags `milestone/baseline-agent` and `milestone/tdd-v1`; their folders were removed from `results/experiments/`.

## Results

| | Baseline | TDD agent v1 (tests given per method) |
| --- | --- | --- |
| Classes passed | **51/100** (50 in the run, 51 after regrading) | **97/100** |
| Tests passed | 1990/2196 (90.6%) | 2168/2196 (98.7%) |
| LLM calls per class | 1 | 3.9 (387 calls over 100 classes) |
| Failing classes | 49 | 25, 31, 49 |
| Run folder | `results/experiments/baseline_2026-11-19T14-38-59` | `results/experiments/tdd_2026-11-19T14-38-58` |

## Why TDD agent v1 fails its three classes
- **ClassEval_49: 30/36. The benchmark's skeleton omits a method.** `matches_requirements` is in `task["solution_code"]` and in the tests (class `JobMarketplaceTestMatchesRequirements`) but not in `task["skeleton"]` or in any `methods_info[i]`. The agent never sees its docstring or its 6 tests, and the 6 errored tests are exactly those. No agent that follows the skeleton can know the method exists. See `classeval-tests.md`.
- **ClassEval_25: 18/19. Same defect.** `set_cookies` is in `task["solution_code"]` and called by `test_set_cookies`, but it is in neither `task["skeleton"]` nor `methods_info`. The test errors with `AttributeError: 'CookiesUtil' object has no attribute 'set_cookies'` because the agent, following the skeleton, never wrote the method.
- **ClassEval_31: 0/21. An agent failure, not a benchmark one.** The agent's final code file is empty, so the tests fail with `NameError: name 'DataStatistics4' is not defined`. The last reply came back empty after using all 8000 output tokens (`stop_reason: max_tokens`); 7 of the task's 13 calls hit that limit. The agent stored the empty reply as the class, replacing the working code of the first method. Keeping the previous code when a reply is empty would avoid it.
- These are the only tasks in the benchmark whose `task["solution_code"]` has a method that `task["skeleton"]` lacks (besides 22, 43 and 46, whose skeletons do not parse).

The baseline's 49 failing classes were not analysed class by class; the failure analysis was done on the `tdd-own` run (see `results-of-insception-run-for-inconsistencies.md` for the per-test labels and the re-score on `stated` tests).

## A first grouping of the baseline's 49 failing classes (not a class-by-class investigation)

Joining each failing test with its label (both judges, `scripts/rescore_stated.py`):
- **44 of the 49 fail only on tests that are not `stated`**: `unstated` (32 classes), `disputed` between the judges (13), `no_method_info` (12), `contradicts` (7), `other_inconsistency` (2); a class can have failures in several groups.
- **5 fail at least one `stated` test**: ClassEval_14, 39, 45, 67 and 92. These are the classes where the agent's code, rather than the docstring, is the first suspect; they are not yet read.
- The 206 failing tests of the baseline (2196 − 1990) split as `unstated` 101, `disputed` 30, `stated` 28, `no_method_info` 22, `contradicts` 22, `other_inconsistency` 3 (a failing test counts in one group).
- The labels are from LLM judges and not hand-checked, so this says where to look first, not what went wrong in each class.

## Reading the two numbers together
On the tests whose behaviour the docstring states (1480 tests both judges label `stated`), baseline passes 94 of 99 classes and TDD agent v1 98 of 99. The 51 against 97 comes mostly from tests the docstring does not support: baseline passes 65.6% of the `unstated` tests and TDD v1 98.0%.
