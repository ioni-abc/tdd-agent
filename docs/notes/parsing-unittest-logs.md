# Parsing unittest logs (`grading/parser.py`)

How `parse_log` turns unittest's `-v` output into counts. Based on the prototype's `build_record`.

## 1. What the log looks like

Real output: the empty skeleton of `ClassEval_0` run against its tests. It always has three parts, in this order.

**Part A: one progress line per test**
```
test_filter_6 (temp_file.AccessGatewayFilterTestFilter.test_filter_6) ... ok
test_filter_8 (temp_file.AccessGatewayFilterTestFilter.test_filter_8) ... FAIL
```

**Part B: one block per failed test, after all tests have run**
```
======================================================================
FAIL: test_filter_1 (temp_file.AccessGatewayFilterTestFilter.test_filter_1)
----------------------------------------------------------------------
Traceback (most recent call last):
  ...
AssertionError: None is not true
```
`FAIL:` means an assertion was false; `ERROR:` means the code crashed (e.g. `AttributeError`).

**Part C: the summary**
```
Ran 19 tests in 0.003s

FAILED (failures=13)
```

The parser reads only part C's `Ran` line and part B's headers.

## 2. Line by line

### Find the total
```python
ran = re.search(r"^Ran (\d+) tests?", log, re.MULTILINE)
```
- `re.search(pattern, text)`: the **first** match anywhere, as a match object, or `None`.
- `r"..."`: raw string, so `\d` reaches the regex engine unchanged.
- `^`: start of a line. `Ran `: literal text; unittest prints the past tense, so it must be `Ran`, not `Run`.
- `(\d+)`: one or more digits; the parentheses make it **group 1**.
- ` tests?`: the `s` is optional, because unittest writes `Ran 1 test`.
- `re.MULTILINE`: without it, `^` means start of the **whole string**; with it, start of **any line**. The `Ran` line is near the end, so it's needed.

On the example log this matches `'Ran 19 tests'`.

### Turn it into a number
```python
total = int(ran.group(1)) if ran else 0
```
- `ran.group(1)` is the captured text, the string `"19"`; `int(...)` makes it `19`.
- `if ran else 0`: no `Ran` line means `ran` is `None`, and `None.group(1)` would crash. That happens when a timeout kills the process before unittest prints its summary.

### Find every failure header
```python
headers = re.findall(r"^(FAIL|ERROR): (\S+)", log, re.MULTILINE)
```
- `re.findall`: **all** matches, not only the first.
- `(FAIL|ERROR)`: group 1, either word. `: `: literal.
- `(\S+)`: group 2, non-space characters; stops at the space before `(temp_file...)`, so it captures only the test name.
- With two groups, each match is a **tuple**: `[('FAIL', 'test_AccessGatewayFilter'), ('FAIL', 'test_filter_1'), ...]`.

### Count distinct names
```python
fail_names  = {name for kind, name in headers if kind == "FAIL"}
error_names = {name for kind, name in headers if kind == "ERROR"} - fail_names
```
- `{... for ... in ...}`: a **set comprehension**; each name is kept once.
- `for kind, name in headers`: unpacks each tuple.
- `- fail_names`: set subtraction; removes names already counted as failures.

Why: one test can produce two blocks, e.g. it fails and then its `tearDown` crashes (one `FAIL:`, one `ERROR:`, same name). Counting blocks counts it twice; in some tasks that gave more errors than tests. Sets count each test once, and the subtraction makes a test either a failure or an error, never both.

### The arithmetic
```python
failed = len(fail_names)
errored = len(error_names)
passed = total - failed - errored
```
Example: `19 - 13 - 0 = 6`, matching the six `... ok` lines in part A.

## 3. Why not the easier ways

- **Counting `... ok` lines:** a test that prints a warning can split its line in two, so the `ok` lands on another line and is missed.
- **Reading `FAILED (failures=13)`:** those numbers count blocks, not tests, so they double-count.

## 4. Checkpoint results (`ClassEval_0`)

| Code | total | passed | failed | errored |
| --- | --- | --- | --- | --- |
| reference solution | 19 | 19 | 0 | 0 |
| empty skeleton | 19 | 6 | 13 | 0 |

## 5. Regex reference

| Token | Meaning |
| --- | --- |
| `^` | start of line (with `re.MULTILINE`) |
| `\d` / `\d+` | a digit / one or more digits |
| `\S` / `\S+` | a non-space character / one or more |
| `?` | the previous character is optional |
| `(a\|b)` | `a` or `b`, captured as a group |
| `( ... )` | capture group, read with `.group(n)` |
| `re.search` | first match or `None` |
| `re.findall` | all matches; tuples when there are several groups |
