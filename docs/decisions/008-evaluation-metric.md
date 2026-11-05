# 008: Greedy class-level pass@1 as the main metric

- **Status:** Proposed
- **Date:** 2026-11-05

## Context

- ClassEval reports pass@1/3/5 from 5 samples at temperature 0.2, plus greedy pass@1. At 0.2, sampled and greedy pass@1 are nearly equal (GPT-4: 37.6% vs 37.0%), and the gap from pass@1 to pass@5 is small for strong models.
- TGen reports "% solved" from one deterministic run (temperature 0) with dependent remediation rounds.
- An iterating agent effectively gets several tries inside one run; comparing it with single-shot baselines on pass@k mixes up the method with the metric.
- Agents are expensive to run 5 times per task, and time is limited.

## Decision

- Main metric: greedy (temperature 0) **class-level pass@1** on the hidden ClassEval tests.
- Also reported: test-level pass rate next to the skeleton baseline (006), iteration counts, and cost (tokens, LLM calls, time).
- Decoding parameters are set explicitly per run and logged in `run.json`, not inherited from library defaults (see the ClassEval code-vs-paper analysis).
- pass@k with multiple samples only if the budget allows.

## Consequences

- Agents and baselines are compared at equal attempts, with cost shown separately.
