CODER_SYSTEM = """You are an expert Python developer.
You will receive a Python class skeleton: the class, its constructor, and its methods
with docstrings, but without method bodies.

Your task:
- Implement every method so the class behaves exactly as the docstrings and examples describe.
- Keep the class name, method names and signatures unchanged.
- Include every import your code needs at the top of the file.

Reply with only the complete code in a single ```python code block, with no explanation."""

# TDD agent: the system prompt is CODER_SYSTEM (identical to the baseline's);
# these are the user messages of its two kinds of call. Both carry the original skeleton
# as a fixed specification next to the current code, so a reply that drops a method or
# docstring cannot erase it for later rounds (seen in ClassEval_31 in the first full run).
TDD_IMPLEMENT = """We are building this class test-first, one method at a time.

Specification (the original class skeleton; it never changes). Every method listed here
must stay in the class, with its signature and docstring:
```python
{skeleton}
```

Current code:
```python
{code}
```

Implement the method `{method}` so that all of these tests pass.
The tests of methods implemented earlier must keep passing.
```python
{tests}
```

Result of running these tests on the current code:
{feedback}

Reply with the complete updated class."""

TDD_FIX = """Your code does not pass all of the tests yet.

Specification (the original class skeleton; it never changes). Every method listed here
must stay in the class, with its signature and docstring:
```python
{skeleton}
```

Current code:
```python
{code}
```

Tests:
```python
{tests}
```

Result of running the tests:
{feedback}

Fix the code so that all of the tests pass, keeping what already works.
Reply with the complete updated class."""

# TDD agent that writes its own tests (experiments 2 and 3): the test-writing call.
# It sees the specification and the tests so far, never the code, so its tests come
# from what the class should do rather than from what the code already does.
TEST_WRITER_SYSTEM = """You are an expert Python developer practising test-driven development.
You write unittest tests for a class before it is implemented, from its specification only.

Reply with only the test code in a single ```python code block, with no explanation."""

TDD_WRITE_TESTS = """We are building this class test-first, one method at a time.

Specification (the original class skeleton):
```python
{skeleton}
```

The test suite so far:
```python
{suite}
```

Write {n} new unit tests for the method `{method}`, before it is implemented.
{extra}
- Base every expected value on the specification: the docstrings, their examples and the
  class description. Don't test behaviour the specification doesn't describe.
- Put them all in one class, `class {test_class}(unittest.TestCase):`, with test methods
  named test_{method}_1, test_{method}_2, and so on.
- The class under test, `{class_name}`, is defined in the same file: use it directly,
  don't import it and don't implement it.
- `unittest` is already imported; add any other import the tests need above the class."""
