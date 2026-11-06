"""Grade a saved experiment run on all of each task's tests.

From the project root:
    uv run python scripts/grade_run.py baseline_2026-11-06T20-30-00
"""

import argparse

from tdd_agent.dataset import load_tasks
from tdd_agent.grading.grader import grade
from tdd_agent.report import print_summary
from tdd_agent.runs import experiment_dir, load_code, save_records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_name")
    args = parser.parse_args()

    run_dir = experiment_dir(args.run_name)
    if not run_dir.is_dir():
        parser.error(f"no such run: {run_dir}")

    code_by_task = load_code(run_dir)
    tasks = [t for t in load_tasks() if t["task_id"] in code_by_task]
    records = [grade(task, code_by_task[task["task_id"]], task["test"]) for task in tasks]

    save_records(records, run_dir / "grades")
    print_summary(args.run_name, records)


if __name__ == "__main__":
    main()