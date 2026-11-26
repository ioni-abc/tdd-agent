# Checking the benchmark: does each test match its docstring?

Question: ClassEval's docstrings and tests are not always in harmony, so how much of a score measures the agent and how much the benchmark? The check is independent of any agent run.

## Method (`scripts/label_tests.py`, branch `test-method-vs-method-docstring`)

For each test in `task["test"]`, an LLM judge (`claude-haiku-5-5`) reads the docstring of the method it tests (`task["methods_info"][i]["method_description"]`), that method's `solution_code` and the test, and picks one label:

| Label | Meaning |
| --- | --- |
| `stated` | the docstring states what the test checks |
| `unstated` | the docstring does not say it (a convention, a format, an edge case) |
| `contradicts` | the docstring says something different from the test and `solution_code` |
| `other_inconsistency` | neither of the above; the judge names the problem in `reason` |
| `no_method_info` | not judged: the test's class is in no `methods_info[i]["test_class"]` |

Each judged row also has a `MISSING` sentence: the general rule the docstring should add. The test is mapped to its method through `test_class`. Answers are cached per test (file name carries a hash of system prompt and prompt), so a rerun costs nothing.

## Results (2196 tests, `results/analysis/benchmark_labels.csv`)

| Label | Tests | Share of the 2088 judged |
| --- | --- | --- |
| `stated` | 1565 | 75% |
| `unstated` | 418 | 20% |
| `contradicts` | 38 | 1.8% |
| `other_inconsistency` | 67 | 3.2% |
| `no_method_info` | 108 | not judged |

- A random sample of 20 tasks (`--sample 20 --seed 0`) gave the same shares for `stated`, `unstated` and `contradicts` (77%, 21%, 2.5%).
- `contradicts` (38) agrees with the earlier failure analysis (about 40 `docstring_contradicts_solution`). Examples: ClassEval_61 `set_volume` (docstring says `True`, code returns `None`), ClassEval_53 (docstring says case sensitive, code lowercases), ClassEval_97 (docstring example says `False` for `"thirty-two"`).
- The judge also finds contradictions that the `>>>` example check (`results/analysis/docstring_examples.json`, 15 of 961 examples differ, in 12 tasks) cannot: ClassEval_33, 38, 61 and 62 have text-versus-code conflicts without a failing example.
- `unstated` is the main source of noise: 15 of 20 sampled tasks have at least one. Most affected in the sample: ClassEval_65 (13 of 28 tests), ClassEval_38 (11 of 19).

## The `other_inconsistency` group is one pattern

62 of the 67 reasons say the same: **the test is filed under method X but exercises method Y.** It is a copy-paste defect in ClassEval's tests, concentrated in 16 tasks (ClassEval_83: 15, ClassEval_89: 14, ClassEval_60: 10, ClassEval_23: 5, ClassEval_1, 10 and 63: 4 each).

- Example: in ClassEval_1, `test_calculate_sphere_area_2` to `_5` all call `calculate_circle_area`. `calculate_sphere_area` is really tested by one test, `calculate_circle_area` by nine.
- The agent is not treated unfairly: the test calls the method, and the agent implements the whole class. The label only means the mapping from test class to docstring is wrong for these tests.
- First run labelled the four sphere tests `unstated`, with meaningless `MISSING` rules. That is why the catch-all label was added.
- Two rows look different: ClassEval_25 `test_load_cookies_2` (sets an attribute that `load_cookies` never reads; closer to a faulty test) and ClassEval_85 `test_set_target_temperature_1` (verifies through a getter; possibly a judge overreach).

## Known limits of the judge
- Tests that reach a method only through the constructor (ClassEval_12 `create_deck`) were labelled inconsistently: `create_deck_1` and `_4` `stated`, `_2` and `_5` `unstated`, `_3` `other_inconsistency`.
- The labels are not yet hand-checked. Plan: 25 random tests per label, compared with my own labels; aim for about 85% agreement, otherwise a stronger model.

## Reading the data: `scripts/export_tasks.py`

`uv run python scripts/export_tasks.py` writes `results/analysis/tasks_readable/<task_id>.md` for all 100 tasks: skeleton, then for each method its docstring, `solution_code` and tests, each test with its label, reason and `MISSING`. The JSON looks unreadable only because newlines are stored as `\n`.

## Second judge and the re-score (`claude-sonnet-5-5`, `scripts/rescore_stated.py`)

- Sonnet ran over the same 2088 tests (`results/analysis/benchmark_labels_claude-sonnet-5-5.csv`, about $8). Agreement with Haiku: **88.6%** (1850 of 2088). Disagreements are mostly `stated` against `unstated` (107 and 74 tests); `contradicts`: 26 tests are `contradicts` for both judges, 24 more for only one. Two replies were unparsed and stay unjudged.
- **Both judges say `stated`: 1480 tests.** Every run was re-scored on them (`results/analysis/rescore_stated.csv`):

| Run | As graded (classes) | `stated` tests passed | Classes passing all `stated` tests |
| --- | --- | --- | --- |
| baseline | 51/100 | 1452/1480 (98.1%) | 94/99 |
| tdd | 97/100 | 1473/1480 (99.5%) | 98/99 |
| tdd-mixed | 68/100 | 1465/1480 (99.0%) | 96/99 |
| tdd-own | 43/100 | 1451/1480 (98.0%) | 91/99 |

- On the `unstated` tests (294) baseline passes 65.6% and tdd 98.0%; on `contradicts` (26) 15.4% against 100%. The gap between the approaches sits in behaviour the docstring does not support, which tdd learns from the given tests.
- Each run is one sample with sampled decoding, so differences of 3 to 4 classes on the `stated` subset are probably noise.

## Plan for the scores
- Re-score each run (baseline, tdd, tdd-own) on the `stated` tests only (1565 of 2196, 71%), joined with the per-test lines in each run's `grades/*.json`.
- `other_inconsistency` is reported as its own group; `unstated` and `contradicts` plus `MISSING` are the to-do list if docstrings are rewritten later.
