"""Printing summaries of graded runs, shared by all scripts."""

from tdd_agent.grading.grader import GradeRecord


def print_summary(label: str, records: list[GradeRecord]) -> None:
    """How many classes passed, then one line per failed class."""
    failed = [r for r in records if not r.class_passed]
    passed = len(records) - len(failed)

    print(f"======= {label.upper()} =======")
    print(f"{passed}/{len(records)} classes passed")
    for r in failed:
        c = r.counts
        print(
            f"  {r.task_id}: {c.tests_passed}/{c.tests_total} "
            f"({c.tests_failed} failed, {c.tests_errored} errored)"
            f" (timeout: {r.timed_out})"
        )
    print()