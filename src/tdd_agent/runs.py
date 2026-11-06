from pathlib import Path
import json

from tdd_agent import config
from tdd_agent.grading.grader import GradeRecord
from tdd_agent.agents.interface import AgentResult


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

def experiment_dir(run_name: str) -> Path:
    """results/experiments/<run_name>/, e.g. results/experiments/baseline_2026-11-06T20-30-00/."""
    return config.RESULTS_DIR / "experiments" / run_name


def save_run_info(run_dir: Path, info: dict) -> None:
    """run.json: which agent, model and settings produced this run."""
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "run.json").write_text(json.dumps(info, indent=2), encoding="utf-8")


def save_result(run_dir: Path, result: AgentResult) -> None:
    """The agent's code to code/<task_id>.py, its LLM calls to calls/<task_id>.json."""
    (run_dir / "code").mkdir(parents=True, exist_ok=True)
    (run_dir / "calls").mkdir(parents=True, exist_ok=True)
    (run_dir / "code" / f"{result.task_id}.py").write_text(result.code, encoding="utf-8")
    calls = [call.model_dump() for call in result.calls]
    (run_dir / "calls" / f"{result.task_id}.json").write_text(json.dumps(calls, indent=2), encoding="utf-8")


def load_code(run_dir: Path) -> dict[str, str]:
    """task_id -> generated code, for every code/<task_id>.py in the run."""
    return {path.stem: path.read_text(encoding="utf-8") for path in sorted((run_dir / "code").glob("*.py"))}