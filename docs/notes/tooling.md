# Tooling notes

## uv

```bash
uv init --package --python 3.12   # pyproject.toml + src/<name>/ package layout
uv venv                           # create .venv (uv add / uv run also create it on demand)
uv add <package>                  # install and record in pyproject.toml
uv run python script.py           # run inside the project's .venv, no activation needed
uv run --no-project --python 3.12 script.py   # run with another Python, ignoring the project
```

Running a script with a different Python is a uv feature: uv downloads and caches interpreters. Python itself can't.

### Why `from tdd_agent import config` works from any folder

1. `uv run` syncs `.venv` and installs the project as an **editable** package (the `-e` idea: nothing copied, only a pointer to the source).
2. The pointer is a `.pth` file in `.venv/lib/python3.12/site-packages/` holding the path to `src/`.
3. Python reads `.pth` files at startup and adds those paths to `sys.path`; every import searches `sys.path`.

```bash
cat .venv/lib/python3.12/site-packages/*.pth
uv run python -c "import tdd_agent; print(tdd_agent.__file__)"
```

### `src/` layout

All importable code lives in `src/tdd_agent/`. Data, results, docs and config stay outside. The extra `src/` level stops Python from importing the code straight from the project folder, so tests run against the installed package.

### Ruff: lint, sort imports, format

```bash
uv add --dev ruff                         # dev-only dependency
uv run ruff check --select I --fix .      # I = isort rules: sort and group imports
uv run ruff format .                      # formatting
```

In `pyproject.toml`, so every `ruff check --fix` covers it:

```toml
[tool.ruff.lint]
select = ["E", "F", "I"]   # style errors, real bugs (unused imports, undefined names), import order
```

Import groups, in order: standard library, third-party, own package (`tdd_agent`).

## Virtual environments

### Which Python am I using?

```bash
python --version
which python                      # should point into the project's .venv
python -c "import sys; print(sys.version); print(sys.executable)"   # most reliable
echo $VIRTUAL_ENV                 # active venv, or empty
```

### How a venv finds its own packages

Each venv has a `pyvenv.cfg` one folder above `bin/python`. When that interpreter starts, it finds the file and uses the venv's `site-packages`. So a subprocess started with a full venv path needs no activation. Activation only changes the shell's `PATH` so that typing `python` finds the venv's interpreter.

### Two venvs, nested folders

Venvs are tied to an interpreter, not to a folder, so two can sit side by side in one project (`.venv`, `.venv-eval`). Nesting folders works for Python, but `uv run` uses the nearest `pyproject.toml` going up, and VS Code picks one interpreter per opened folder, which is where "wrong Python" bugs come from.

The prototype used two venvs: `agent-venv` (3.12) for `generate_tdd.py`, `.venv` (3.8) for `grade.py`. They never ran in the same process; they communicated only through files on disk.

### VS Code

The interpreter shows in the **bottom right** of the status bar, and only while a `.py` file is the active tab. On macOS, choosing a venv's `python` alias in the file dialog can select the base interpreter it points to; type the path into **Enter interpreter path…** instead.

## macOS

### `/var` is a symlink to `/private/var`

Temp folders live under `/var/folders/...`. When `subprocess.run` gets a full file path and `cwd` set to the temp folder, unittest computes the path relative to `cwd`; with one side resolved to `/private/var/...` and the other still `/var/...`, the result starts with `..` and unittest uses the path as a module name:

```
ModuleNotFoundError: No module named '/var/folders/.../temp_file'
```

Fix: pass only the file name, since it is relative to `cwd` by definition.

## Git and GitHub

- **Author vs pusher:** the author is the name and email in the commit (`git config user.name/user.email`); the pusher is the GitHub account that pushes. GitHub links a commit to a profile only if the author email is verified on that account.
- **Co-author:** a `Co-Authored-By:` line at the end of the message makes GitHub show a second avatar.
- **"Unverified" label:** the commit is signed with a key not registered on the account. Commits from Claude's workspace are signed automatically with the workspace's own key, hence the label.
- **Paths in git commands are relative to the current folder.** From `src/tdd_agent/`, `git rm --cached src/tdd_agent/x.txt` fails with "pathspec did not match"; use `x.txt`, or `cd` to the root. `git status` prints paths relative to where you are.
- **Check before adding:** `git status` before `git add .`, or add specific paths (`git add src/tdd_agent/grading pyproject.toml uv.lock`). A stray log file inside `src/` got committed this way.
- **Taking a file out of an unpushed commit:** `git rm --cached <file>` (keeps it on disk), then `git commit --amend --no-edit`. Only safe before pushing.
- **`remote: Internal Server Error` on push:** a problem on GitHub's side; nothing was pushed. Retry after a minute; githubstatus.com shows outages.
- **Claude GitHub app:** *authorized* (Settings → Applications → Authorized GitHub Apps) is not the same as *installed* (Installed GitHub Apps). Without the install, Claude only sees public repos; new private repos must be added under the app's repository access.
