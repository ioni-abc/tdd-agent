# 010: ClassEval's test packages in a separate `eval` dependency group, pinned for compatibility

- **Status:** Accepted
- **Date:** 2026-11-05

## Context

The first benchmark run on the project venv failed 15 classes, 12 of them with `0/1 (0 failed, 1 errored)`: the test file couldn't be imported because third-party packages were missing. ClassEval's tests and reference solutions import them; `tdd_agent` itself does not.

Installing the latest versions fixed most tasks but broke two:

- `ClassEval_51`: NumPy 2.0 removed `np.mat`, used by the reference solution.
- `ClassEval_69`: the **test** file imports `reportlab`, which was not installed.

Pinning `numpy<2` then conflicted with the latest pandas (3.1.1 requires `numpy>=2.3.3`), so pandas had to be pinned too.

## Decision

- Test-only packages go in a dependency group, separate from the project's real dependencies:

  ```bash
  uv add --group eval numpy pandas python-docx openpyxl gensim beautifulsoup4 pillow nltk PyPDF2
  uv add --group eval "numpy<2" "pandas<3" reportlab
  ```

- Pins: `numpy<2` (ClassEval was written against NumPy 1.x, `numpy~=1.22`) and `pandas<3` (the 2.x line works with NumPy 1.x).
- `tdd_agent`'s own imports (e.g. `pydantic`) go in `dependencies`; dev tools (Ruff) in the `dev` group.

## Consequences

- `pyproject.toml` shows which packages belong to the benchmark and which to the system.
- If another task fails with an import error or a removed API, the fix is a pin in this group, recorded here.
- Open: limit `requires-python` to `">=3.12,<3.13"`, so uv doesn't resolve for Python versions the project never runs on, and the environment the results came from is stated exactly.
