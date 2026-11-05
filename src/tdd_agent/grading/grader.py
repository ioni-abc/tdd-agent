from pydantic import BaseModel

from tdd_agent.grading.parser import TestCounts, parse_log
from tdd_agent.grading.runner import run_tests


class GradeRecord(BaseModel):
    task_id: str
    counts: TestCounts
    class_passed: bool
    log: str


def grade(task: dict, code: str) -> GradeRecord:
    log = run_tests(code=code, test_code=task["test"])
    test_counts = parse_log(log=log)
    return GradeRecord(
        task_id=task["task_id"],
        counts=test_counts,
        class_passed=test_counts.tests_total > 0 and (test_counts.tests_passed == test_counts.tests_total),
        log=log
    )
