from tdd_agent.dataset import load_tasks
from tdd_agent.grading.grader import GradeRecord, grade
from tdd_agent.runs import reference_dir, save_records
from tdd_agent.report import print_summary

REFERENCE_RUNS = {
    "benchmark": "solution_code",
    "skeleton": "skeleton"
}

def run(tasks: list[dict], code_key: str) -> list[GradeRecord]:
    return [grade(task, task[code_key], task["test"]) for task in tasks]

def main() -> None:
    tasks = load_tasks()
    for label, code_key in REFERENCE_RUNS.items():
        records = run(tasks, code_key)
        save_records(records, reference_dir(label))
        print_summary(label, records)

if __name__ == "__main__":
    main()
