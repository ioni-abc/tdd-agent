"""Write data/ClassEval_data_fixed.json: the original data with the fixes in data/test_fixes.json applied.

The original file is never modified. A fix targets either the tests (the default) or the
reference solution:

- "target": "test"           -> task["test"] and methods_info[i]["test_code"]
- "target": "solution_code"  -> task["solution_code"] and methods_info[i]["solution_code"]

Each fix is applied to the task-level text and to the per-method copies, so the two stay
consistent. Run from the project root:
    uv run python scripts/fix_benchmark.py
"""

import json

from tdd_agent import config

# target -> (field on the task, field on each methods_info entry)
FIELDS = {
    "test": ("test", "test_code"),
    "solution_code": ("solution_code", "solution_code"),
}


def apply_fix(task: dict, fix: dict) -> None:
    task_field, method_field = FIELDS[fix.get("target", "test")]
    found = task[task_field].count(fix["old"])
    if found != fix["count"]:
        raise ValueError(
            f"{fix['task_id']}: expected {fix['count']} occurrence(s) of the old text "
            f"in {task_field}, found {found}"
        )
    task[task_field] = task[task_field].replace(fix["old"], fix["new"])
    for method in task["methods_info"]:
        if method[method_field]:
            method[method_field] = method[method_field].replace(fix["old"], fix["new"])


def main() -> None:
    tasks = json.loads(config.DATA_PATH.read_text(encoding="utf-8"))
    fixes = json.loads(config.TEST_FIXES_PATH.read_text(encoding="utf-8"))
    by_id = {task["task_id"]: task for task in tasks}

    for fix in fixes:
        apply_fix(by_id[fix["task_id"]], fix)
        print(f"fixed {fix['task_id']} ({fix.get('target', 'test')}: {fix['where']})")

    config.FIXED_DATA_PATH.write_text(json.dumps(tasks, indent=2), encoding="utf-8")
    print(f"wrote {config.FIXED_DATA_PATH.name}: {len(fixes)} fixes")


if __name__ == "__main__":
    main()
