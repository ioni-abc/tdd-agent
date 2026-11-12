CODER_SYSTEM = """You are an expert Python developer.
You will receive a Python class skeleton: the class, its constructor, and its methods
with docstrings, but without method bodies.

Your task:
- Implement every method so the class behaves exactly as the docstrings and examples describe.
- Keep the class name, method names and signatures unchanged.
- Include every import your code needs at the top of the file.

Reply with only the complete code in a single ```python code block, with no explanation."""

# TDD agent: the system prompt is CODER_SYSTEM (identical to the baseline's);
# these are the user messages of its two kinds of call.
TDD_IMPLEMENT = """We are building this class test-first, one method at a time.

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