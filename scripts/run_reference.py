"""Grade ClassEval's reference solutions ("benchmark") and empty skeletons.

From the project root:
    uv run python scripts/run_reference.py              # on the fixed data (default)
    uv run python scripts/run_reference.py --original   # on ClassEval's original, unfixed data

Results are saved to results/reference/<label>/, or results/reference/<label>_original/ with --original.
"""

import argparse

from tdd_agent.dataset import load_tasks
from tdd_agent.grading.grader import GradeRecord, grade
from tdd_agent.report import print_summary
from tdd_agent.runs import reference_dir, save_records

REFERENCE_RUNS = {
    "benchmark": "solution_code",
    "skeleton": "skeleton"
}


def run(tasks: list[dict], code_key: str) -> list[GradeRecord]:
    return [grade(task, task[code_key], task["test"]) for task in tasks]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--original", action="store_true", help="use ClassEval's original data, without the test fixes")
    args = parser.parse_args()

    tasks = load_tasks(fixed=not args.original)
    suffix = "_original" if args.original else ""
    for label, code_key in REFERENCE_RUNS.items():
        records = run(tasks, code_key)
        save_records(records, reference_dir(label + suffix))
        print_summary(label + suffix, records)


if __name__ == "__main__":
    main()
