import ast
import json
import math

from tdd_agent import config


def load_tasks(fixed: bool = True) -> list[dict]:
    """Load ClassEval's tasks; with fixed=True (default) the copy with the broken tests fixed."""
    path = config.FIXED_DATA_PATH if fixed else config.DATA_PATH
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def clean_skeleton(task: dict) -> str:
    """ Some ClassEval's skeletons are wrapped in '''...''' """
    skeleton = task["skeleton"].strip()
    if skeleton.startswith("'''") and skeleton.endswith("'''"):
        skeleton = skeleton[3:-3].strip()
    return skeleton


def test_header(task: dict) -> str:
    """The imports at the top of the task's test file. The per-method test copies don't have them."""
    return task["test"].split("\nclass ", 1)[0] + "\n"


def tests_for_method(task: dict, method: dict) -> str:
    """The tests the agent receives for one method.

    The seam for a later visible/hidden split (ADR 011): today it returns the method's
    full test class; a split would return only the visible part, without changing any agent.
    """
    return method["test_code"] or ""


def split_method_tests(test_code: str, ratio: float) -> tuple[str, int, int]:
    """Keep the first ceil(ratio * n) of a method's n test methods (experiment 3).

    setUp, tearDown and other helpers stay. Returns the kept test class, how many tests
    it keeps and how many the method had. ClassEval's test_code is one test class.
    """
    if not test_code.strip():
        return "", 0, 0
    lines = test_code.splitlines()
    cls = ast.parse(test_code).body[0]

    def start(node) -> int:
        return min([node.lineno] + [d.lineno for d in getattr(node, "decorator_list", [])])

    tests = [n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name.startswith("test")]
    keep = math.ceil(ratio * len(tests))
    dropped = {id(n) for n in tests[keep:]}
    header = "\n".join(lines[start(cls) - 1 : start(cls.body[0]) - 1])
    members = ["\n".join(lines[start(n) - 1 : n.end_lineno]) for n in cls.body if id(n) not in dropped]
    return header + "\n" + "\n\n".join(members), keep, len(tests)


def select_tests(test_code: str, names: set[str]) -> str:
    """Keep only the test methods whose names are in `names` (held-out experiment).

    setUp, tearDown and other helpers stay. ClassEval's test_code is one test class.
    Returns "" when no test is kept.
    """
    if not test_code.strip() or not names:
        return ""
    lines = test_code.splitlines()
    cls = ast.parse(test_code).body[0]

    def start(node) -> int:
        return min([node.lineno] + [d.lineno for d in getattr(node, "decorator_list", [])])

    def is_test(n) -> bool:
        return isinstance(n, ast.FunctionDef) and n.name.startswith("test")

    kept = [n for n in cls.body if not is_test(n) or n.name in names]
    header = "\n".join(lines[start(cls) - 1 : start(cls.body[0]) - 1])
    members = ["\n".join(lines[start(n) - 1 : n.end_lineno]) for n in kept]
    return header + "\n" + "\n\n".join(members)


def method_test_names(test_code: str) -> list[str]:
    """The names of the test methods in one method's test class, in file order."""
    if not test_code.strip():
        return []
    cls = ast.parse(test_code).body[0]
    return [n.name for n in cls.body if isinstance(n, ast.FunctionDef) and n.name.startswith("test")]


def methods_in_order(task: dict) -> list[dict]:
    """The task's methods, each one after the methods it calls (its method_dependencies).

    Keeps ClassEval's order where dependencies allow. A cycle can't be ordered, so
    its remaining methods follow in ClassEval's order.
    """
    remaining = list(task["methods_info"])
    done: set[str] = set()
    ordered = []
    while remaining:
        ready = next(
            (m for m in remaining if set(m["dependencies"]["method_dependencies"]) <= done),
            remaining[0],  # cycle: take the first left
        )
        ordered.append(ready)
        done.add(ready["method_name"])
        remaining.remove(ready)
    return ordered
