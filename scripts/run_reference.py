from tdd_agent.dataset import load_tasks
from tdd_agent.grading.grader import GradeRecord, grade

REFERENCE_RUNS = {
    "benchmark": "solution_code",
    "skeleton": "skeleton"
}

def run(tasks: list[dict], code_key: str) -> list[GradeRecord]:
    return [grade(task, task[code_key]) for task in tasks]

def print_summary(label: str, records: list[GradeRecord]) -> None:
    failed = [r for r in records if not r.class_passed]
    passed = len(records) - len(failed)

    print(f"======= {label.upper()} =======")
    print(f"{passed}/{len(records)} classes passed")
    for r in failed:
        c = r.counts
        print(
            f"  {r.task_id}: {c.tests_passed}/{c.tests_total} "
            f"({c.tests_failed} failed, {c.tests_errored} errored)"
        )
    print()

def main() -> None:
    tasks = load_tasks()
    for label, code_key in REFERENCE_RUNS.items():
        records = run(tasks, code_key)
        print_summary(label, records)

if __name__ == "__main__":
    main()
