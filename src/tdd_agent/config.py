from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "ClassEval_data.json"  # original, never edited
FIXED_DATA_PATH = PROJECT_ROOT / "data" / "ClassEval_data_fixed.json"  # written by scripts/fix_benchmark.py
TEST_FIXES_PATH = PROJECT_ROOT / "data" / "test_fixes.json"  # the fix log
RESULTS_DIR = PROJECT_ROOT / "results"
TIMEOUT_SECONDS = 5  # per test run, as in the ClassEval paper and the prototype
