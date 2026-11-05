import subprocess
import sys
import tempfile
from pathlib import Path


def run_tests(code: str, test_code: str) -> str:
    with tempfile.TemporaryDirectory() as tmpdriname:
        tmpfile = Path(tmpdriname) / "temp_file.py"
        tmpfile.write_text(code + "\n" + test_code)
        res = subprocess.run(
            [sys.executable, "-m", "unittest", "-v", "temp_file.py"],
            capture_output=True,
            text=True,
            cwd=tmpdriname,
        )
    return res.stderr
