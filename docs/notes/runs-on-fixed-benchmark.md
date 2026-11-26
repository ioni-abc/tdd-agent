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

Two are defects in the benchmark's class outline (`task["skeleton"]`), which also fail the baseline in the same way; one is a failure of the agent. Line numbers refer to the readable per-task files (`results/analysis/tasks_readable/ClassEval_<n>.md`, made by `scripts/export_tasks.py`).

| Class | TDD v1 | Baseline | Kind |
| --- | --- | --- | --- |
| ClassEval_25 | 18/19 | 18/19 | benchmark: a method the tests call is not in the skeleton |
| ClassEval_49 | 30/36 | 30/36 | benchmark: a helper is named but its signature and behaviour are not stated |
| ClassEval_31 | 0/21 | 12/21 | agent: empty replies replaced the class |

### ClassEval_25: 18/19, the method `set_cookies` is not in the skeleton
- **What fails:** `test_set_cookies` (class `CookiesUtilTestSetCookies`) with `AttributeError: 'CookiesUtil' object has no attribute 'set_cookies'`. The other 18 tests pass.
- **Where the method is:** `task["solution_code"]` defines it:
  ```python
  def set_cookies(self, request):
      request['cookies'] = '; '.join([f'{key}={value}' for key, value in self.cookies.items()])
  ```
  `task["skeleton"]` does not, and neither does `task["methods_info"]` (its three entries are `get_cookies`, `load_cookies`, `_save_cookies`).
- **What the agent was told:** the skeleton defines four methods (`__init__`, `get_cookies`, `load_cookies`, `_save_cookies`; lines 13, 21, 32, 42 of the readable file). The only mention is in the class description (line 10): "methods for retrieving, saving, and setting Cookies data". It gives no method name, parameter (`request`) or behaviour.
- **The test:** lines 346 to 364. Line 362 calls `self.cookies_util.set_cookies(request)`. Its class is in no `methods_info[i]["test_class"]`, so it is labelled `no_method_info`, and TDD v1 never received it.
- **Result:** both agents implemented exactly the four methods of the skeleton (the baseline's code defines the same four), and both fail this one test.
- **Verdict:** benchmark defect. No agent that follows the skeleton can know the method, its name or its parameter.

### ClassEval_49: 30/36, a helper named in one docstring, signature and behaviour unstated
- **What fails:** six tests: `test_matches_requirements` to `_5` (class `JobMarketplaceTestMatchesRequirements`, lines 618 to 663 of the readable file) and `test_main` (line 685). TDD v1's error is `AttributeError: 'list' object has no attribute 'get'`.
- **The skeleton does not define `matches_requirements`.** It is named only inside the docstring of `get_job_applicants` (line 536 of the readable file): "... by calling the matches_requirements function". So the agent knew the name and wrote its own helper:
  - TDD v1: `@staticmethod matches_requirements(resume, job)`, which reads `job.get('requirements', [])` and checks that the resume's skills cover every requirement. The baseline wrote `matches_requirements(self, resume, job)`.
  - `task["solution_code"]`: `@staticmethod matches_requirements(resume, requirements)`, which takes the list of requirements directly and returns `False` if any skill of the resume is not in it (the opposite direction).
- **The tests** call it as `matches_requirements({...resume...}, ['skill1', 'skill2'])`. The agent's helper receives a list where it expects a job dict, so `job.get` fails.
- **Why the agent could not get it right:** the name appears in the skeleton, but the argument order, the argument types and the direction of the check appear nowhere. The 5 tests of the helper are in no method's test class, so TDD v1 never saw them; the sixth is the class-level `test_main`.
- **Result:** the same 30/36 for both agents. The other 30 tests pass, including the tests of `get_job_applicants`, which uses the agent's own helper.
- **Verdict:** benchmark defect (unstated behaviour of a helper). This replaces my earlier wording that the agent "never sees the method".

### ClassEval_31: 0/21, the agent's final class is empty
- **What fails:** all 21 tests error with `NameError: name 'DataStatistics4' is not defined`, because the agent's saved code (`results/experiments/tdd_2026-11-19T14-38-58/code/ClassEval_31.py`) is empty.
- **The run's calls** (`calls/ClassEval_31.json`, 13 calls, `steps/ClassEval_31.json`): 1 for `correlation_coefficient` (passes its 5 tests), then 1 implementation call plus 3 fix calls for each of `skewness`, `kurtosis` and `pdf`.
- **8 of the 13 calls ended with `stop_reason: max_tokens`** at the limit of 8000 output tokens. Five of them returned an empty reply (0 characters), and three returned code cut off in the middle (1990, 2583 and 500 characters). The other five calls ended normally.
- **The harness keeps the last reply as the class.** The last call (the third fix attempt for `pdf`) came back empty, so the final code is empty. Earlier steps show the same effect: after the fix attempts for `skewness` the suite found 0 tests (the code did not run), and for `kurtosis` the class passed only 10 of 15 tests.
- **Where the 8000 tokens went is not visible:** the saved call holds only the reply text, which is empty or short, so the budget was probably used by something that is not in it (for example hidden reasoning). I have not checked.
- **The baseline** answers this class with one call and passes 12 of 21 tests, so the class itself can be solved for part of its tests; the 21 tests all pass on `task["solution_code"]`.
- **Verdict:** agent failure, not a benchmark defect. A rule that keeps the previous non-empty class when a reply is empty or cut off would have avoided losing the code; not tried.

The baseline's 49 failing classes were not analysed class by class; the failure analysis was done on the `tdd-own` run (see `results-of-insception-run-for-inconsistencies.md` for the per-test labels and the re-score on `stated` tests).

## A first grouping of the baseline's 49 failing classes (not a class-by-class investigation)

Joining each failing test with its label (both judges, `scripts/rescore_stated.py`):
- **44 of the 49 fail only on tests that are not `stated`**: `unstated` (32 classes), `disputed` between the judges (13), `no_method_info` (12), `contradicts` (7), `other_inconsistency` (2); a class can have failures in several groups.
- **5 fail at least one `stated` test**: ClassEval_14, 39, 45, 67 and 92. These are the classes where the agent's code, rather than the docstring, is the first suspect; they are not yet read.
- The 206 failing tests of the baseline (2196 − 1990) split as `unstated` 101, `disputed` 30, `stated` 28, `no_method_info` 22, `contradicts` 22, `other_inconsistency` 3 (a failing test counts in one group).
- The labels are from LLM judges and not hand-checked, so this says where to look first, not what went wrong in each class.

## Reading the two numbers together
On the tests whose behaviour the docstring states (1480 tests both judges label `stated`), baseline passes 94 of 99 classes and TDD agent v1 98 of 99. The 51 against 97 comes mostly from tests the docstring does not support: baseline passes 65.6% of the `unstated` tests and TDD v1 98.0%.
