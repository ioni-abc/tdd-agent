# 011: TDD agent v1 receives all of ClassEval's tests, method by method

- **Status:** Accepted for the 13 Nov meeting; the split (below) to be discussed with the professor
- **Date:** 2026-11-06

## Context

- The original plan had the agent write its own tests (agent_3). The professor was not keen: ClassEval already provides tests, and an agent writing weak tests would make the TDD loop look bad for reasons unrelated to TDD. It also mixes two skills in one measurement.
- ClassEval is organised per method: 409 of 410 methods have their own test class in `methods_info[i]["test_code"]` (most have 5 tests; `ClassEval_69.merge_pdfs` has none). That is a ready-made one-method-at-a-time feed.
- Prior work (TGen) gives the model tests and grades on separate private tests. ClassEval has no separate private tests.
- Grading an agent on the tests it was given answers a weaker question: it can pass without implementing the behaviour, the score saturates near 100% with a fix loop, and a win over the baseline (which sees no tests) can be attributed to access to the tests.

## Decision

**Version 1 (for the meeting):** the agent receives ClassEval's tests, one method at a time, and is graded on all tests.

**Possible extension (after the meeting, if the professor agrees):** split each method's tests into visible (about 60%, `k = max(1, min(n - 1, round(0.6 * n)))`) and hidden; the agent sees only the visible ones; class-level test classes are always hidden. Both agents are then graded on the hidden tests (the fair comparison) and on all tests (comparable with the paper). Within one agent, the gap between the two shows how much it fitted to its visible tests.

Two seams make the extension a swap rather than a rewrite:

1. The agent gets its tests from one function, `tests_for_method(task, method)`, never from `methods_info` directly.
2. `grade(task, code, test_code)` takes the tests to run as an argument.

Saved generated code means the baseline (which sees no tests) only needs re-grading on hidden tests, not regenerating.

## Consequences

- v1 results carry the weakness above; they are presented as v1, with the split as the planned next step and an explicit question to the professor.
- External numbers (ClassEval's paper) are context only; the result is the controlled comparison baseline vs TDD, same model and tasks. Prior work is connected by reimplementing its approach (holistic = baseline; TGen-style batch variant) rather than by comparing numbers.
