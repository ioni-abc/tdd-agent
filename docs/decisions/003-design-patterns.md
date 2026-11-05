# 003: Design patterns used, and those avoided

- **Status:** Accepted
- **Date:** 2026-11-05

## Context

The module split (001) leaves open how agents are swapped, how the flow is wired, and how components get their tools. Patterns are introduced at the step where they solve a real problem, not up front.

## Decision

| Pattern | Where | What it solves |
| --- | --- | --- |
| **Strategy** | `agents/` | Baseline, TDD-batch and TDD-incremental share one interface, `generate(task) -> AgentResult`, so one script runs any agent. Implemented with a `Protocol`, not a base class. |
| **Pipe and filter** | the overall flow | `dataset → generate → (files) → grade → (files) → report`; each stage reads and writes files, so a run can be re-graded without regenerating. (Sommerville, Ch. 6) |
| **Dependency injection** | agents | An agent receives its LLM client and test runner (constructor arguments) instead of creating them: models can be switched, and a fake client allows testing without API calls. |
| **Functional core, imperative shell** | `grading/` | `parse_log` is pure (string in, dict out) and trivial to unit-test; `run_tests` and `runs.py` hold the side effects. |
| **Repository** | `runs.py` | All knowledge of the results folder layout lives in one module. (Sommerville, Ch. 6) |
| **Registry** | `scripts/generate.py` | Once there are two or more agents: `AGENTS = {"baseline": ..., "tdd": ...}`, so agents are chosen by name on the command line. |

**Avoided:** Template Method and inheritance hierarchies for agents (they get in the way once agents diverge); plugin systems, factories and abstract base classes everywhere (too heavy for about three variants and the time available).

## Consequences

- A new agent is one new file in `agents/`; the scripts and the grader don't change.
- Each pattern can be named and justified in the thesis's design chapter.
