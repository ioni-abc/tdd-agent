from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "ClassEval_data.json"
RESULTS_DIR = PROJECT_ROOT / "results"
TIMEOUT_SECONDS = 5  # per test run, as in the ClassEval paper and the prototype