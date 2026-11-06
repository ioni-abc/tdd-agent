"""Write data/ClassEval_data_fixed.json: the original data with the fixes in data/test_fixes.json applied.

The original file is never modified. Every fix is applied to the task's full test suite
(task["test"]) and to the per-method copies (methods_info[i]["test_code"]), so the two stay
consistent. Run from the project root:
    uv run python scripts/fix_benchmark.py
"""

import json

from tdd_agent import config


def apply_fix(task: dict, fix: dict) -> None:
    found = task["test"].count(fix["old"])
    if found != fix["count"]:
        raise ValueError(
            f"{fix['task_id']}: expected {fix['count']} occurrence(s) of the old text, found {found}"
        )
    task["test"] = task["test"].replace(fix["old"], fix["new"])
    for method in task["methods_info"]:
        if method["test_code"]:
            method["test_code"] = method["test_code"].replace(fix["old"], fix["new"])


def main() -> None:
    tasks = json.loads(config.DATA_PATH.read_text(encoding="utf-8"))
    fixes = json.loads(config.TEST_FIXES_PATH.read_text(encoding="utf-8"))
    by_id = {task["task_id"]: task for task in tasks}

    for fix in fixes:
        apply_fix(by_id[fix["task_id"]], fix)
        print(f"fixed {fix['task_id']} ({fix['test']})")

    config.FIXED_DATA_PATH.write_text(json.dumps(tasks, indent=2), encoding="utf-8")
    print(f"wrote {config.FIXED_DATA_PATH.name}: {len(fixes)} fixes")


if __name__ == "__main__":
    main()
