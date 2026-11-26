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
- **ClassEval_49: 30/36, the 6 errored tests are exactly its hidden tests.** The agent sees tests only through the per-method copies (`methods_info[i]["test_code"]`); 4.9% of the tests (107 of 2196) are in no copy. See `classeval-tests.md`.
- **ClassEval_25: 18/19.** `test_set_cookies` errors with `AttributeError: 'CookiesUtil' object has no attribute 'set_cookies'`: the agent's class has no such method.
- **ClassEval_31: 0/21.** All 21 tests error with `NameError: name 'DataStatistics4' is not defined`.

The baseline's 49 failing classes were not analysed class by class; the failure analysis was done on the `tdd-own` run (see `results-of-insception-run-for-inconsistencies.md` for the per-test labels and the re-score on `stated` tests).

## Reading the two numbers together
On the tests whose behaviour the docstring states (1480 tests both judges label `stated`), baseline passes 94 of 99 classes and TDD agent v1 98 of 99. The 51 against 97 comes mostly from tests the docstring does not support: baseline passes 65.6% of the `unstated` tests and TDD v1 98.0%.
