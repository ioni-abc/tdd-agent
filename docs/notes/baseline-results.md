# The first full baseline run

Run `baseline_2026-11-06T20-14-18`: `claude-haiku-5-5`, one sampled call per task (temperature not settable, ADR 014), fixed data, graded on all tests.

## Result

| | |
| --- | --- |
| Classes passed | **48/100** |
| Tokens | 97,224 in, 178,963 out |
| Time | about 11 minutes (2–22 s per task) |

For context only (different model, prompt, year): ClassEval's paper reported 37% class-level pass@1 for GPT-4 with the holistic strategy.

## The 52 failures

- **Near misses:** about 20 classes miss by only 1–2 tests, e.g. `ClassEval_2` 20/21, `ClassEval_18` 36/37, `ClassEval_96` 21/22, `ClassEval_0` 17/19. This is where a red → fix → green loop should help: the agent sees the failing test and gets another try. A concrete thing to check in the TDD results.
- **Large misses:** e.g. `ClassEval_14` 1/7, `ClassEval_92` 5/21, `ClassEval_40` 8/16.
- **Crashes before any test ran:** `ClassEval_48` (`0/1`) and `ClassEval_69` (`0/3`): the test file couldn't load, so likely an import or syntax problem in the generated code. Worth checking whether it's the model or `extract_code`.

## Reading it

- One sampled run per task is a noisy measurement (ADR 014). A difference of a few points between agents needs more than one sample before it is claimed.
- Command to reproduce the grading: `uv run python scripts/grade_run.py baseline_2026-11-06T20-14-18`.
