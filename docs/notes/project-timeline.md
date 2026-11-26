# Project timeline: what was done, in order, and what each step produced

Oldest at the top. Numbers are classes passed out of 100 (tests passed out of 2196 where given).

## 1. Setup and reference run
- Reference solutions (`task["solution_code"]`) run against `task["test"]`: **96/100**.
- Five broken tasks diagnosed; fixes kept as data in `data/test_fixes.json`, applied by `scripts/fix_benchmark.py` to `data/ClassEval_data_fixed.json` (the original is never edited). Reference run again: **100/100**.
- Produced: `results/reference/`, `data/test_fixes.json`, `data/ClassEval_data_fixed.json`, notes `reference-run.md`, `benchmark-fixes.md`.

## 2. Baseline (docstrings in, code out)
- Empty skeletons score 0/100 (only 157 of 2124 tests pass by accident).
- Baseline: **48** → **50** → **51** (1990/2196 tests, 90.6%) after fixes and regrading.
- Produced: `results/experiments/baseline_2026-11-19T14-38-59`, note `baseline-results.md`.

## 3. TDD with the given tests (`tdd`)
- The agent sees `test_code` of each method (about 95% of graded tests) and loops until they pass.
- **96** → **97** (2168/2196 tests, 98.7%) after a skeleton fix.
- Produced: `results/experiments/tdd_2026-11-19T14-38-58`, note `tdd-agent.md`.

## 4. TDD with its own tests (`tdd-own`)
- The agent writes its own tests, then code. **42** → **43** (1954/2196, 89.0%) after rejecting wrong written tests (ClassEval_22, 43, 46, 48).
- Its own tests on its own code: 2040/2050 (99.5%); on `task["solution_code"]`: 1917/2050.
- Produced: `results/experiments/tdd-own_2026-11-19T14-38-57`.

## 5. Mixed (`tdd-mixed`)
- Part given tests, part own tests: **68**. Not rerun after the fixes (on hold).
- Produced: `results/experiments/tdd-mixed_2026-11-19T14-38-56`.

## 6. Failure analysis (`scripts/analyse_failures.py`)
- 242 failing tests in 57 classes of `tdd-own`; about 89% are benchmark-side (docstring does not state the behaviour: `unstated_behaviour`; about 40 real `docstring_contradicts_solution`; 30 `no_method_info`).
- Docstring examples run against `task["solution_code"]`: 15 of 961 differ, in 12 tasks.
- Produced: `<run>/analysis/failures.csv`, `summary.json`, `results/analysis/docstring_examples.json` (written on 19 Nov).

## 7. Meeting with the professor (20 Nov) and rethink
- Concern: the docstrings and the tests of ClassEval are not in harmony, so the scores partly measure the benchmark.
- Decision: check the benchmark itself, independent of any agent run.

## 8. Branch cleanup (25 Nov)
- Tags on the tips of `tdd-mixed-tests` and `failure-analysis`, fast-forward merge into `main` (tip 6e9fee5), redundant branches deleted. `docs` stays separate.

## 9. Benchmark check (branch `test-method-vs-method-docstring`)
- `scripts/label_tests.py`: an LLM judge (claude-haiku-5-5) labels each of the 2088 tests that have a method as `stated`, `unstated` or `contradicts` against the method's docstring, with a `MISSING` sentence.
- Next: run it on ClassEval_1, 4 and 92, hand-check about 100 labels, then re-score every run on the `stated` tests only (Option A) and use `unstated`/`contradicts` plus `MISSING` as the docstring rewrite list.
- Meeting with the professor: Fri 27 Nov.
