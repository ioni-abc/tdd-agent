# Python notes

## Paths

### `str` vs `Path`

`tempfile.TemporaryDirectory()` gives a plain string. `Path(...)` wraps it in a `pathlib.Path`, which is what makes `/` joining and `.write_text()` work.

```python
"/tmp/abc" / "file.py"          # TypeError: unsupported operand type(s) for /: 'str' and 'str'
Path("/tmp/abc") / "file.py"    # PosixPath('/tmp/abc/file.py')
```

`subprocess.run(cwd=...)` accepts either type.

### `Path.cwd()` vs `Path(__file__)`

| | Based on | Breaks when |
| --- | --- | --- |
| `Path.cwd()` | the folder you **run** the command from | you run from a different folder |
| `Path(__file__)` | the folder the **file** is in | you move the file itself |

Experiment (from `src/tdd_agent/config.py`): `cwd` changed between running from the project root and from `src/tdd_agent/`; `Path(__file__).resolve().parents[2]` stayed `.../tdd-agent` both times.

### `resolve()` and `parents[n]`

- `resolve()`: absolute path, `..` removed, symlinks followed, so `parents[]` climbs the real folders.
- `parents[0]` is the file's own folder, `parents[1]` one up, and so on.

```python
PROJECT_ROOT = Path(__file__).resolve().parents[2]   # src/tdd_agent/config.py -> tdd-agent/
```

Since Python 3.9 the running script's `__file__` is already absolute, so `resolve()` usually changes nothing. It matters when the file is reached through a symlink: without it, `parents[2]` walks up from the symlink's location instead of the real file's.

## Modules and imports

### Importing a module should not do work

`config.py` holds only constants; `dataset.py` reads the JSON inside `load_tasks()`, not at module level. The prototype's `grade.py` loaded 2.3 MB at import time, so merely importing it read the file.

### Relative vs absolute imports

```python
from . import config            # relative: "the config next to me"; survives renaming the package
from tdd_agent import config    # absolute: easier to read
```

Both work. Pick one style for the whole project.

## Functions

### `lambda` vs `def`

A lambda holds one *expression*, so it can't contain `with`. PEP 8 says not to assign lambdas to names: tracebacks show `<lambda>`, and there are no type hints or docstring. Lambdas are for throwaway functions passed to something else:

```python
sorted(tasks, key=lambda t: t["class_name"])
```

### `json.load` vs `json.loads`

```python
json.load(f)                              # from a file object
json.loads(path.read_text(encoding="utf-8"))   # from a string
```

Always pass `encoding="utf-8"` when reading text files; the default encoding differs between machines.

## Temp files and subprocesses

### `tempfile.TemporaryDirectory()`

Creates the folder when the `with` block starts and deletes it, with everything inside, when the block ends. No `mkdir()` needed: it would raise `FileExistsError`.

### `subprocess.run([...])`

The list is the exact command. The first item is the program to start; passing a full interpreter path decides which Python runs. `sys.executable` is the Python running the current script.

It returns a `CompletedProcess` with `.returncode`, `.stdout` and `.stderr`. unittest writes its results to **stderr**; `stdout` stays empty.
