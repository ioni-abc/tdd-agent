# Does the agent notice when a given test does not fit the docstring? (flag only)

Code: `scripts/doubt_check.py` and `DOUBT_SYSTEM`, `DOUBT_CHECK` in `src/tdd_agent/prompts.py`, branch `test-method-vs-method-docstring`. Model: `claude-haiku-5-5`. One sample.

## What was asked
- One call per method (410 methods, 2088 tests). The agent sees what TDD agent v1 sees for a method: the docstring (`methods_info[i]["method_description"]`) and the method's test class (`methods_info[i]["test_code"]`). It never sees `solution_code`.
- For each test it answers `CONSISTENT`, `SILENT` (the docstring does not say what the test expects) or `CONTRADICTS`.
- Flag only: nothing is fed back into code writing, so no red/green loop was run.
- The answers are compared with the per-test labels in `results/analysis/benchmark_labels.csv`.

## Results (tests per label, and what the agent answered)

| Label | Tests | CONSISTENT | SILENT | CONTRADICTS | Unparsed |
| --- | --- | --- | --- | --- | --- |
| `stated` | 1572 | 1445 (91.9%) | 77 (4.9%) | 1 (0.1%) | 49 (3.1%) |
| `unstated` | 414 | 87 (21.0%) | 282 (68.1%) | 16 (3.9%) | 29 (7.0%) |
| `contradicts` | 44 | 8 (18.2%) | 10 (22.7%) | 26 (59.1%) | 0 |
| `other_inconsistency` | 58 | 18 (31.0%) | 34 (58.6%) | 6 (10.3%) | 0 |

## Reading
- **It notices.** On the 44 `contradicts` tests the agent raises a flag (`SILENT` or `CONTRADICTS`) on 36 (81.8%). It says exactly `CONTRADICTS` on 26 (59.1%).
- **The flags are not random.** On `stated` tests it raises a flag on 78 of 1572 (5.0%). On `unstated` tests it flags 298 of 414 (72.0%).
- **Of the 452 tests it flagged, 374 (82.7%) are not `stated`** by the label.
- **Contrast with TDD agent v1:** given the same tests, v1 passes all 44 `contradicts` tests (`runs-on-fixed-benchmark.md`). It follows the tests when it is only asked to make them pass, although the same model can see the mismatch when asked directly.

## Caveats
- **Not independent.** The labels come from a Haiku judge (which also saw `solution_code`) and the check is Haiku too, so agreement between them does not prove either is right. The labels are not checked by hand.
- **Small group.** `contradicts` has 44 tests.
- **Unparsed:** 78 tests (49 `stated`, 29 `unstated`) were not in a parseable reply line and are not counted as flags.
- **Asked directly.** The check is a separate question. It shows the agent can see the mismatch, not that it would raise it unprompted inside the loop.

## Next
- Hand-check a sample of the labels, stratified by label.
- Second version: pass the flagged tests back to the agent with the instruction to follow the docstring, and compare its results with v1's.
