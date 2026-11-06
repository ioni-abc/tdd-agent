from pathlib import Path

from tdd_agent import config
from tdd_agent.grading.grader import GradeRecord


def reference_dir(label: str) -> Path:
    """results/reference/<label>/, e.g. results/reference/benchmark/."""
    return config.RESULTS_DIR / "reference" / label


def save_records(records: list[GradeRecord], run_dir: Path) -> None:
    """Write one <task_id>.json per record into run_dir."""
    run_dir.mkdir(parents=True, exist_ok=True)
    for record in records:
        (run_dir / f"{record.task_id}.json").write_text(
            record.model_dump_json(indent=2), encoding="utf-8"
        )


def load_records(run_dir: Path) -> list[GradeRecord]:
    """Read every <task_id>.json in run_dir back into GradeRecords, sorted by file name."""
    return [
        GradeRecord.model_validate_json(path.read_text(encoding="utf-8"))
        for path in sorted(run_dir.glob("*.json"))
    ]