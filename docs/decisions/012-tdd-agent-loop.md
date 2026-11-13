# 012: The TDD agent's loop

- **Status:** Accepted, implemented in `agents/tdd.py` (2026-11-12)
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

## As implemented (2026-11-12)

```
code  = clean skeleton
suite = test header (the imports from task["test"])

for method in methods_in_order(task):
    suite += tests_for_method(task, method)
    RED    run suite on code
           already green -> record it, write no code, next method
    CODE   one call: TDD_IMPLEMENT (code, method name, whole suite, red feedback)
    GREEN  run suite; while red and attempts < 3: one call TDD_FIX (code, suite, failures)
    record a MethodStep
```

- **No code without a failing test:** if the suite is already green at the red step, the method gets no call (`coded: false`). The model often writes more than the one method asked for, so later methods are frequently green already; this is Beck's rule and saves calls.
- **Max 3 fix attempts** per method, then the agent moves on with its last code; the step records `green: false`.
- **The model rewrites the whole class at every call** (it gets the current code and returns the complete class); the growing suite is the regression check.
- **Same system prompt as the baseline** (`CODER_SYSTEM`); only the user messages differ (`TDD_IMPLEMENT`, `TDD_FIX` in `prompts.py`), so the comparison isolates the method.
- **Feedback to the model** (`feedback()`): a summary line ("3 of 5 tests pass") plus unittest's failure blocks, capped at 4,000 characters; a timeout or a crash before any test ran gets a short explanation plus the end of the log.
- **Injected test runner** (`TDDAgent(llm, max_fix_attempts=3, run=run_tests)`), like the LLM.
- **Step log**, per method, saved to `steps/<task_id>.json` via a new `AgentResult.steps` field: `method`, `tests_in_suite`, `red_passed`, `coded`, `fix_attempts`, `green_passed`, `green`.
- **Class-level test classes** (not tied to a method) are never shown to the agent: `tests_for_method` only returns per-method test classes. They are graded at the end. Measured: 107 of 2,196 tests (4.9%) in 88 tasks; a side effect, too small and uneven to count as a held-out set (see `notes/classeval-tests.md`).
- **Method order** (`methods_in_order`): repeatedly the first remaining method whose `method_dependencies` are done; on a cycle, the first remaining. On the data: 28 tasks reordered, 3 cycles; `ClassEval_0` becomes `is_start_with`, `get_jwt_user`, `set_current_user_info_and_log`, `filter`.
- **Check of the per-method test files** (header + one method's tests vs the reference solution): 366 pass. One real quirk: `ClassEval_25.load_cookies`' tests only pass if another method's test has written `cookies.json` first; in the TDD loop earlier methods' tests are in the suite too.
- Tested end to end with a fake LLM before any API call.

## Consequences

- The loop reuses `run_tests` with a growing suite; since the project uses one environment (007), green during generation means green at grading.
- Each test file built from `methods_info` needs the import header from `task["test"]` (the per-method copies start directly with `class ...`), and the split, if added, must keep `setUp`/`tearDown` in both halves (82 method test classes have them).
