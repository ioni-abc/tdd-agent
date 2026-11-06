# 014: Sampled decoding at the API's fixed temperature; samples per task as a parameter

- **Status:** Accepted
- **Date:** 2026-11-06
- **Supersedes:** 008

## Context

- Anthropic's API version `2026-10-21`, used by `anthropic` 2.x (2.6.0 installed), removed `temperature`, `top_p` and `top_k`. A request that sends them fails (in the SDK: `TypeError: Messages.create() got an unexpected keyword argument 'temperature'`), and nothing replaces them. Requests sample with the defaults, including temperature 1.0.
- Claude 4.7 and later models, including `claude-haiku-5-5`, already accept only the defaults, so pinning the older API version would not bring temperature 0 back either.
- So every run is **sampled**: the same agent on the same task can produce different code. Decision 008 (greedy pass@1, temperature 0) can't be carried out.

Source: [Migrating to API version 2026-10-21](https://platform.claude.com/docs/en/api/migration-2026-10-21).

## Decision

- No sampling parameters are sent. `run.json` records the temperature as "API default (1.0, not settable since API version 2026-10-21)".
- The model is fixed per comparison: `config.MODEL = "claude-haiku-5-5"` for both agents.
- **For the 13 Nov meeting:** one sample per task per agent. Results are presented as single sampled runs, with that limitation stated.
- **Next step:** n samples per task (e.g. n = 3). Then pass@1 = correct ÷ n averaged over tasks (the unbiased estimator; less noisy than one sample), and pass@3 from the same runs. The number of samples is to be a parameter of the run, so this needs no rework.
- Still reported, as in 008: test-level pass rate next to the skeleton baseline, iteration counts, and cost (tokens, LLM calls, time).

## Consequences

- One run per task is a noisy measurement; differences between agents of a few percentage points need n > 1 before they are claimed.
- "Current Claude models can't be run deterministically" is a limitation to name in the thesis, and a point to raise with the professor.
