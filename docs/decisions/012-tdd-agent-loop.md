# 012: The TDD agent's loop

- **Status:** Proposed (to be confirmed when the loop is built, step C1)
- **Date:** 2026-11-06

## Context

The meeting needs a TDD agent that actually runs tests in a red/green loop. The prototype's `generate_tdd.py` ran nothing: its tests were only extra text in the prompt.

## Decision

```
code  = skeleton
suite = []

for method in methods, ordered so that method_dependencies come first:
    suite += tests_for_method(task, method)
    1. RED    run suite on code    -> this method's tests should fail
    2. CODE   LLM implements the method; sees current code + suite + failing output
    3. GREEN  run suite            -> all pass: next method
              still red            -> send failures back, fix, up to N tries (e.g. 3); then move on anyway

finally: grade the class
```

- **Per method, not per single test:** one method's tests at a time (about 3x fewer calls). One test at a time is future work.
- **Method order from `methods_info[i]["dependencies"]["method_dependencies"]`:** in `ClassEval_0`, `filter` is listed first but calls the other three methods; implementing it first would make its tests fail because the helpers don't exist yet.
- **Red is observed, not required:** some tests already pass on the empty skeleton (`ClassEval_0`: 6 of 19). The red step records them as "green before implementation" rather than stopping.
- **The regression suite:** earlier methods' tests are re-run at every green step, catching an agent that breaks a finished method.
- **Never stuck:** after N failed fix tries the agent keeps its best code, records the failure, and continues.
- **Recorded per method:** red and green results, number of tries, tokens.
- **Not in v1:** a refactor step; one-test-at-a-time; frameworks such as LangGraph (a plain Python loop is easier to explain and debug).

The baseline is one call from the skeleton (ClassEval's holistic strategy). A TDD-batch variant (all tests up front, then the fix loop, TGen-style) is optional.

## Consequences

- The loop reuses `run_tests` with a growing suite; since the project uses one environment (007), green during generation means green at grading.
- Each test file built from `methods_info` needs the import header from `task["test"]` (the per-method copies start directly with `class ...`), and the split, if added, must keep `setUp`/`tearDown` in both halves (82 method test classes have them).
