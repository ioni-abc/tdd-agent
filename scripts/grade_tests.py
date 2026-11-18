"""Grade a run's test suites on ClassEval's reference solution: are the agent's tests right?

A test that fails on the reference solution expects behaviour the specification doesn't
have, so code made to pass it is wrong. Saves to <run>/tests_on_solution/.

From the project root:
    uv run python scripts/grade_tests.py tdd-own_2026-11-19T10-00-00
"""

import argparse

from tdd_agent.dataset import load_tasks
from tdd_agent.grading.grader import grade
from tdd_agent.runs import experiment_dir, load_code, save_records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_name")
    args = parser.parse_args()

    run_dir = experiment_dir(args.run_name)
    suites = load_code(run_dir, folder="tests")
    if not suites:
        parser.error(f"no tests/ in {run_dir} (only TDD runs save their suites)")

    tasks = [t for t in load_tasks() if t["task_id"] in suites]
    records = [grade(task, task["solution_code"], suites[task["task_id"]]) for task in tasks]
    save_records(records, run_dir / "tests_on_solution")

    passed = sum(r.counts.tests_passed for r in records)
    total = sum(r.counts.tests_total for r in records)
    all_right = sum(r.class_passed for r in records)
    print(f"======= {args.run_name.upper()}: TESTS ON THE REFERENCE SOLUTION =======")
    print(f"{passed}/{total} tests pass on the reference solution ({passed / max(total, 1):.1%})")
    print(f"{all_right}/{len(records)} suites pass completely")
    for r in records:
        if not r.class_passed:
            print(f"  {r.task_id}: {r.counts.tests_passed}/{r.counts.tests_total} (timeout: {r.timed_out})")


if __name__ == "__main__":
    main()
