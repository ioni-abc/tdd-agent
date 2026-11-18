import json

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
