import subprocess
import sys
import tempfile
from pathlib import Path

from pydantic import BaseModel

from tdd_agent import config


class RunOutput(BaseModel):
    log: str
    timed_out: bool


def run_tests(code: str, test_code: str, timeout: float = config.TIMEOUT_SECONDS) -> RunOutput:
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpwd = Path(tmpdir)
        (tmpwd / "temp_file.py").write_text(code + "\n" + test_code, encoding="utf-8")
        try:
            res = subprocess.run(
                [sys.executable, "-m", "unittest", "-v", "temp_file.py"],
                capture_output=True,
                text=True,
                cwd=tmpwd,
                timeout=timeout,
            )
            return RunOutput(log=res.stderr, timed_out=False)
        except subprocess.TimeoutExpired as e:
            partial = e.stderr.decode() if isinstance(e.stderr, bytes) else (e.stderr or "")
            return RunOutput(log=partial, timed_out=True)

