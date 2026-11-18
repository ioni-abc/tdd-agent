"""Turning an LLM's test-writing reply into a test class the suite can use (experiments 2 and 3)."""

import ast


class UnusableTests(ValueError):
    """The reply can't go into the suite; the message is sent back to the LLM."""


def clean_tests(text: str, test_class: str, class_name: str) -> tuple[str, int]:
    """Keep the reply's test code, minus anything that would break the suite.

    Drops a copy of the class under test (it would replace the agent's code) and any
    import of it (there is no module to import it from), and `if __name__ == ...` blocks.
    Returns the cleaned code and its number of test methods.
    """
    try:
        tree = ast.parse(text)
    except SyntaxError as e:
        raise UnusableTests(f"The tests are not valid Python: {e}") from e

    lines = text.splitlines()
    kept, count = [], None
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            continue
        if isinstance(node, ast.ImportFrom) and any(a.name == class_name for a in node.names):
            continue
        if isinstance(node, ast.If):
            continue
        if isinstance(node, ast.ClassDef) and node.name == test_class:
            count = sum(
                1 for n in node.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name.startswith("test")
            )
        start = min([node.lineno] + [d.lineno for d in getattr(node, "decorator_list", [])])
        kept.append("\n".join(lines[start - 1 : node.end_lineno]))

    if count is None:
        raise UnusableTests(f"There is no class named {test_class}.")
    if count == 0:
        raise UnusableTests(f"{test_class} has no test methods (their names must start with test).")
    return "\n\n".join(kept), count
