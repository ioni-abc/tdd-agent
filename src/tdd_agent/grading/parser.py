import re

from pydantic import BaseModel


class TestCounts(BaseModel):
    tests_total: int
    tests_passed: int
    tests_failed: int
    tests_errored: int


def parse_log(log: str) -> TestCounts:
    ran = re.search(r"^Ran (\d+) tests?", log, re.MULTILINE)
    total = int(ran.group(1)) if ran else 0
    headers = re.findall(r"^(FAIL|ERROR): (\S+)", log, re.MULTILINE)
    fail_names = {name for kind, name in headers if kind == "FAIL"}
    error_names = {name for kind, name in headers if kind == "ERROR"} - fail_names
    failed = len(fail_names)
    errored = len(error_names)
    passed = total - failed - errored
    return TestCounts(
        tests_total=total,
        tests_passed=passed,
        tests_failed=failed,
        tests_errored=errored,
    )
