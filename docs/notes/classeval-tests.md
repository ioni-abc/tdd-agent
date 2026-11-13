# How ClassEval's tests are organised

## Per method

Each method in `methods_info` has its own test class:

| `ClassEval_0` method | Test class | Tests |
| --- | --- | --- |
| `filter` | `AccessGatewayFilterTestFilter` | 8 |
| `is_start_with` | `AccessGatewayFilterTestIsStartWith` | 5 |
| `get_jwt_user` | `AccessGatewayFilterTestGetJwtUser` | 5 |
| `set_current_user_info_and_log` | `AccessGatewayFilterTest` | 1 |

Across the dataset: 410 methods, 409 with tests (`ClassEval_69.merge_pdfs` has none). Tests per method: 310 methods have exactly 5, 12 have only 1, the most is 12. 88 tasks have test classes that appear in none of the per-method copies (see "Class-level tests" below).

## Class-level tests

A **method-level test** calls one method and checks only that. A **class-level test** calls several methods in one test, usually in sequence on the same object, to check that they work together. A class can pass every method-level test and still fail at class level, e.g. when one method leaves the fields in a state another doesn't expect. ClassEval counts a class as correct only if it passes both.

```python
# method-level: only precedence
def test_precedence_1(self):
    calculator = Calculator()
    self.assertEqual(calculator.precedence('+'), calculator.precedence('-'))

# class-level: calculate, precedence and apply_operator in one test
def test_calculator(self):
    calculator = Calculator()
    self.assertEqual(calculator.calculate('1+2'), 3)
    res1 = calculator.precedence('+')
    ...
    calculator.apply_operator(operand_stack, operator_stack)
```

**Where they are:** in the same `task["test"]` field as everything else; there is no separate field. `task["test"]` for `ClassEval_16` holds four test classes: `CalculatorTestCalculate` (8 tests), `CalculatorTestPrecedence` (5), `CalculatorTestApplyOperator` (5) and the class-level `CalculatorTest` (1).

| | Stored | Used by |
| --- | --- | --- |
| Method tests | in `task["test"]` **and** copied in `methods_info[i]["test_code"]` | the TDD agent (via the copies) and the grader |
| Class-level tests | in `task["test"]` only | the grader only |

**Why not in `methods_info`:** that list has one entry per method (description, reference code, its own tests). A class-level test belongs to no single method, so there is no entry to put it under. To spot them: a name in `task["test_classes"]` that is no method's `"test_class"`.

**What the TDD agent gets:** the whole skeleton (`task["skeleton"]`), each round the method's name and its `test_code`. Not `method_description` (the same signature and docstring are already in the skeleton), and never the class-level tests.

## Tests the TDD agent never sees (measured 2026-11-13)

A test is "hidden" here when it is in `task["test"]` but in none of the per-method copies.

- **107 of 2,196 tests (4.9%)** are hidden; the agent sees the other 95%.
- 88 tasks have hidden tests, 12 have none.

| Hidden tests in the task | Tasks |
| --- | --- |
| 0 | 12 |
| 1 | 77 |
| 2 | 7 |
| 3 or more | 4 (`ClassEval_7`: 3, `ClassEval_82`: 3, `ClassEval_57`: 4, `ClassEval_49`: 6) |

The 12 with none: `ClassEval_0`, `14`, `34`, `35`, `53`, `60`, `62`, `63`, `71`, `83`, `89`, `97`. Either the task has no class-level test class, or it is filed under a method (as in `ClassEval_0`), so the agent receives it. For these 12 the agent is graded only on tests it saw.

**This split is a side effect, not a design.** In ClassEval's own experiments models see no tests at all, so nobody chose what to hide. It exists only because our agent takes its tests from the per-method copies. It is too small (4.9%) and too uneven (0 to 6 per task) to serve as a held-out set, which is the argument for a deliberate split (ADR 011).

**`ClassEval_49` shows why held-out tests matter:** in the full TDD run it scored 30/36 with 6 errored, exactly its 6 hidden tests. One hidden class, `JobMarketplaceTestMatchesRequirements`, covers a method that `methods_info` doesn't list, so the agent never got tests for it. It passed everything it saw and failed everything it didn't.

## Where the data departs from the paper

Section 3.2.3 of the ClassEval paper states the test-construction rules. The released data (commit `eaeac44`) doesn't fully follow them, and the paper doesn't mention the exceptions (its threats to validity cover data leakage and benchmark size).

| Paper's rule | In the data |
| --- | --- |
| "at least five test cases" for each method | 12 methods have only 1 test; `ClassEval_69.merge_pdfs` has none |
| class-level tests "with different combinations of methods under test, ensuring that each method is invoked at least once in the class-level tests" | 12 tasks have no separate class-level test class |
| (implied) tests map cleanly to methods | the class-level test class is filed under a method in some tasks (`ClassEval_0`); in `ClassEval_49` a test class covers a method missing from `methods_info` |

Together with the five broken tasks (ADR 005), this is evidence that the benchmark is hand-made and has rough edges that only show when it is run and inspected.

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
