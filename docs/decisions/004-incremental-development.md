# 004: Build module by module, simplest version first

- **Status:** Accepted
- **Date:** 2026-11-05

## Context

The prototype is being rewritten for this repo. The goal is a code base I understand in every part, not only a working one.

## Decision

- Build one module at a time, each function in its simplest form first, and expand it later, even when part of its job will move to another function a few steps on.
- Each increment ends with a command to run and its expected output (a checkpoint). If a step has no checkpoint, it's too big.
- One increment, one commit.
- Design decisions are settled when they appear in the code, unless they must be made up front (e.g. the results layout, before the first save).
- Workflow per step: Claude gives the goal, signature and expected result; I write the code; we review; then commit. Hints before code when stuck.

Planned order: `config.py` → `dataset.py` → `grading/runner.py` → `grading/parse.py` → `grading/grade.py` → `scripts/run_reference.py` → `runs.py` → timeouts, failure reasons, `KNOWN_BROKEN` → `llm.py` → agents → `scripts/generate.py`.

## Consequences

- The history shows how the design evolved, step by step.
- Step 6 (reference runs) is checked against the prototype's numbers: matching results confirm the rewrite.
