# How ClassEval's tests are organised

## Per method

Each method in `methods_info` has its own test class:

| `ClassEval_0` method | Test class | Tests |
| --- | --- | --- |
| `filter` | `AccessGatewayFilterTestFilter` | 8 |
| `is_start_with` | `AccessGatewayFilterTestIsStartWith` | 5 |
| `get_jwt_user` | `AccessGatewayFilterTestGetJwtUser` | 5 |
| `set_current_user_info_and_log` | `AccessGatewayFilterTest` | 1 |

Across the dataset: 410 methods, 409 with tests (`ClassEval_69.merge_pdfs` has none). Tests per method: 310 methods have exactly 5, 12 have only 1, the most is 12. 89 tasks have one or two class-level test classes not tied to a method.

## Things to know when building test files

- **No imports in the per-method copies.** `methods_info[i]["test_code"]` starts directly with `class ...`; only `task["test"]` begins with `import unittest` (and other imports). Any test file built from the per-method copies needs that header on top, or it fails with `NameError: unittest`.
- **`setUp` / `tearDown`:** 82 method test classes have them; any split must keep them in both halves.
- **Two copies of every test:** each test exists in `task["test"]` and in its method's `test_code`. Fixes must change both (decision 005).
- **Order:** `methods_info` order is not dependency order. In `ClassEval_0`, `filter` comes first but calls the other three. `dependencies["method_dependencies"]` gives the order to implement them in.

## The other fields

| Field | What it is | Used for |
| --- | --- | --- |
| `methods_info[i]["test_code"]` | that method's test class | the per-method feed for the TDD agent |
| `methods_info[i]["test_class"]` | its test class name | telling method tests from class-level tests |
| `methods_info[i]["dependencies"]` | `method_`, `field_`, `lib_dependencies` | method order; DEP(M)/DEP(F) analysis |
| `methods_info[i]["method_description"]` | one method's signature + docstring | the "implement this method" prompt |
| `methods_info[i]["solution_code"]` | reference code for one method | debugging and test audits, never agents |
| `test_classes` | all test class names | finding the class-level ones |
| `import_statement`, `class_constructor`, `class_description` | pieces of the skeleton | building the code incrementally |
| `fields` | the `self.` fields | DEP(F) analysis |

## The visible/hidden split, by example (possible extension, decision 011)

Every "set of tests" is just a **string of test code**; the grader takes whichever string it is given. With `is_start_with` and `get_jwt_user` (5 tests each, first 3 visible):

**All tests:** `task["test"]`, unchanged.

**Hidden tests**, built once, used only for the final grade:

```python
import unittest

class AccessGatewayFilterTestIsStartWith(unittest.TestCase):
    def test_is_start_with_4(self): ...
    def test_is_start_with_5(self): ...

class AccessGatewayFilterTestGetJwtUser(unittest.TestCase):
    def test_get_jwt_user_4(self): ...
    def test_get_jwt_user_5(self): ...
```

**Visible tests so far**, which grow as the agent works. While on `get_jwt_user`, method 1's visible tests stay (the regression suite):

```python
import unittest

class AccessGatewayFilterTestIsStartWith(unittest.TestCase):
    def test_is_start_with_1(self): ...
    def test_is_start_with_2(self): ...
    def test_is_start_with_3(self): ...

class AccessGatewayFilterTestGetJwtUser(unittest.TestCase):
    def test_get_jwt_user_1(self): ...
    def test_get_jwt_user_2(self): ...
    def test_get_jwt_user_3(self): ...
```

Who uses which:

```python
grade(task, code, visible_so_far)   # inside the agent's loop
grade(task, code, hidden)           # final, the fair score
grade(task, code, task["test"])     # final, comparable with the paper
```

## Reading the results table

Compare **between agents, on the same test set**, column by column:

| Agent | Hidden tests | All tests |
| --- | --- | --- |
| Baseline | 40% | 42% |
| TDD | 55% | 70% |

*(made-up numbers)*

- **Hidden column = the verdict:** neither agent saw these tests.
- **All-tests column = context:** comparable with the paper's setup, but biased toward TDD, which saw 60% of them.
- **Within one row = a diagnostic:** a big gap means the agent fitted to its visible tests rather than the behaviour.

## Why grading on seen tests is weak

1. The agent can pass without solving the problem (`return uri in ('/api/data', '/login/data')`).
2. With a fix loop, scores saturate near 100%, so variants can't be told apart.
3. A win over the baseline can be attributed to access to the tests rather than to TDD.
4. Real code has to work beyond its tests.

But: TGen uses "passes the public tests" as its main criterion in RQ1–3, and ClassEval's tests are thorough (99.7% statement coverage). Reporting both is the defensible setup.

## Splitting in code (`ast`)

`ast.parse(test_code)` → find the class and its `def test_*` methods in file order → first k visible, rest hidden; everything else (`setUp`, `tearDown`, helpers) in both → `ast.unparse` each half. Rule: `k = max(1, min(n - 1, round(0.6 * n)))` (1 → 1/0, 2 → 1/1, 5 → 3/2, 8 → 5/3). Class-level test classes always hidden.
