from pydantic import BaseModel

from tdd_agent.grading.parser import TestCounts, parse_log
from tdd_agent.grading.runner import run_tests


class GradeRecord(BaseModel):
    task_id: str
    counts: TestCounts
    class_passed: bool
    timed_out: bool
    log: str


def grade(task: dict, code: str, test_code: str) -> GradeRecord:
    run = run_tests(code=code, test_code=test_code)
    counts = parse_log(log=run.log)
    return GradeRecord(
        task_id=task["task_id"],
        counts=counts,
        class_passed=counts.tests_total > 0 and (counts.tests_passed == counts.tests_total) and not run.timed_out,
        timed_out=run.timed_out,
        log=run.log
    )
