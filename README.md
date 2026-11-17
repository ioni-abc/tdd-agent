# tdd-agent

> 🚧 **Work in progress.** This is the code for my MSc thesis in Software Design at the IT University of Copenhagen, due January 2027.

## The idea

Most LLM code generators write a whole class in one go. Test-Driven Development builds code in small steps instead: a failing test, then just enough code to pass it, then a refactor, and repeat.

This thesis asks whether an **LLM agent that works through tests one at a time** writes more correct class-level code than a single-shot generator. The single-shot baseline is ClassEval's "holistic" strategy. Related work such as [TGen](https://arxiv.org/abs/2402.13521) gives the model all the tests at once; this project gives it tests **incrementally**, with a growing regression suite and a refactor step.

## Benchmark

The tasks come from **[ClassEval](https://github.com/FudanSELab/ClassEval)** (Du et al., 2023, [arXiv:2308.01861](https://arxiv.org/abs/2308.01861)): 100 hand-written Python classes, each with a skeleton (signatures and docstrings only), a reference solution and unit tests.

## Findings so far

| Run | Classes passing all tests | Tests passed |
|---|---|---|
| Reference solutions (after fixes) | 100 / 100 | 2196 / 2196 |
| Empty skeletons | 0 / 100 | 157 / 2124 |
| **Baseline agent** (Claude Haiku 5.5, one call per class) | **48 / 100** | 1959 / 2181 (89.8%) |

- **The benchmark itself had 5 broken tasks.** One test was a time bomb (dated 2024), one depended on the original author's laptop, two compared floats exactly, and one reference solution had a bug. The fixes are logged in [`data/test_fixes.json`](data/test_fixes.json) and applied by a script. The original data is never edited.
- **The single-shot baseline passes most tests but under half of the classes.** Its mistakes are small but spread out, which leaves room for an iterative, test-by-test agent to improve.

## Next steps

- [ ] TDD agent: receives ClassEval's tests one at a time and works in a red → green → refactor loop
- [ ] Variant with held-out tests, so the agent never sees the tests it is graded on
- [ ] Compare against the baseline: pass rate, cost (tokens) and number of iterations
- [ ] Validate on real open-source Python projects

## How it works

```
src/tdd_agent/
  dataset.py          load ClassEval tasks (original or fixed)
  llm.py              thin wrapper around the Anthropic API, logs tokens and time
  agents/             Agent interface (Strategy pattern) + baseline agent
  grading/            run tests in a subprocess with a timeout → parse the log → grade
scripts/
  fix_benchmark.py    apply data/test_fixes.json → ClassEval_data_fixed.json
  run_reference.py    grade the reference solutions and empty skeletons
  generate.py         run an agent over the tasks, save code + LLM calls
  grade_run.py        grade a saved run
results/              reference runs and experiment runs (code, calls, grades)
```

```bash
uv sync
echo "ANTHROPIC_API_KEY=..." > .env
uv run python scripts/fix_benchmark.py
uv run python scripts/generate.py baseline
uv run python scripts/grade_run.py <run_name>
```
