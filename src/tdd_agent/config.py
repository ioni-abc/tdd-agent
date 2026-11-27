from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "ClassEval_data.json"  # original, never edited
FIXED_DATA_PATH = PROJECT_ROOT / "data" / "ClassEval_data_fixed.json"  # written by scripts/fix_benchmark.py
TEST_FIXES_PATH = PROJECT_ROOT / "data" / "test_fixes.json"  # the fix log
RESULTS_DIR = PROJECT_ROOT / "results"
TIMEOUT_SECONDS = 5  # per test run, as in the ClassEval paper and the prototype
MODEL = "claude-haiku-5-5"
MAX_TOKENS = 8000
HELD_OUT_SPLIT_PATH = PROJECT_ROOT / "data" / "held_out_split.json"  # written by scripts/make_split.py
