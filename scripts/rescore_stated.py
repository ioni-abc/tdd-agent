"""Re-score every experiment run on the tests both judges labelled `stated`.

Joins the per-test lines of each run's grades/<task>.json (the `log` field) with the labels of
scripts/label_tests.py, by (task_id, test class, test name). A test belongs to the group
  stated               both judges say stated (the spec-consistent subset)
  unstated, contradicts, other_inconsistency   both judges agree on that label
  disputed             the two judges disagree
  no_method_info       class-level tests, not judged
For each run it reports the pass rate per group and two class counts:
  - classes passing all tests (as graded; matches the run's own count)
  - classes passing all their `stated` tests (classes without a stated test are left out)

From the project root (after label_tests.py with both models):
    uv run python scripts/rescore_stated.py
    uv run python scripts/rescore_stated.py --runs baseline_2026-11-19T14-38-59,tdd_2026-11-19T14-38-58
Writes results/analysis/rescore_stated.csv (one row per run and group).
"""

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from tdd_agent import config

ANALYSIS = config.RESULTS_DIR / "analysis"
HAIKU_CSV = ANALYSIS / "benchmark_labels.csv"
STRONG_CSV = ANALYSIS / "benchmark_labels_claude-sonnet-5-5.csv"
OUT_CSV = ANALYSIS / "rescore_stated.csv"
GROUPS = ["stated", "unstated", "contradicts", "other_inconsistency", "disputed", "no_method_info"]

# "test_x (temp_file.TestClass.test_x) ... ok" -> test, class, rest of the line
HEADER = re.compile(r"^(\S+) \(.*?(\w+)\.(\w+)\) \.\.\. ?(.*)$")
STATUS = ("ok", "FAIL", "ERROR")


def read_labels(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return {(r["task_id"], r["test_class"], r["test"]): r["label"] for r in csv.DictReader(f)}


def group_of(first: str, second: str) -> str:
    """The group of a test, from the two judges' labels."""
    if first == "no_method_info":
        return "no_method_info"
    if first == second:
        return first
    return "disputed"


def parse_log(log: str) -> dict:
    """(test class, test) -> True if it passed. A warning printed between a test's header and
    its status pushes the status to a later line of its own, so that case is followed up."""
    out, open_test = {}, None
    for line in log.splitlines():
        m = HEADER.match(line)
        if m:
            open_test, rest = (m.group(2), m.group(1)), m.group(4).strip()
            if rest in STATUS:
                out[open_test], open_test = rest == "ok", None
        elif open_test and line.strip() in STATUS:
            out[open_test], open_test = line.strip() == "ok", None
    return out


def run_results(run_dir: Path) -> dict:
    """(task_id, test class, test) -> passed, for every test of the run."""
    results = {}
    for path in run_dir.glob("grades/*.json"):
        grade = json.loads(path.read_text(encoding="utf-8"))
        for (cls, test), ok in parse_log(grade["log"]).items():
            results[(grade["task_id"], cls, test)] = ok
    return results


def score(results: dict, group: dict) -> tuple[dict, dict]:
    """Pass counts per group, and class counts: (all tests, all stated tests)."""
    by_group = defaultdict(lambda: [0, 0])
    all_ok, stated_ok, stated_n = defaultdict(lambda: True), defaultdict(lambda: True), Counter()
    for key, ok in results.items():
        all_ok[key[0]] &= ok
        if key not in group:
            continue
        by_group[group[key]][0] += ok
        by_group[group[key]][1] += 1
        if group[key] == "stated":
            stated_n[key[0]] += 1
            stated_ok[key[0]] &= ok
    classes = {
        "all_passed": sum(all_ok.values()),
        "all_total": len(all_ok),
        "stated_passed": sum(stated_ok[t] for t in stated_n),
        "stated_total": len(stated_n),
    }
    return by_group, classes


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--runs", help="comma-separated run folder names (default: every run in results/experiments)")
    args = parser.parse_args()

    first, second = read_labels(HAIKU_CSV), read_labels(STRONG_CSV)
    group = {key: group_of(first[key], second[key]) for key in first if key in second}
    runs = args.runs.split(",") if args.runs else sorted(p.name for p in (config.RESULTS_DIR / "experiments").iterdir())

    rows = []
    for name in runs:
        by_group, classes = score(run_results(config.RESULTS_DIR / "experiments" / name), group)
        print(f"\n{name}")
        for g in GROUPS:
            passed, total = by_group[g]
            if total:
                print(f"  {g:20s} {passed}/{total} = {passed / total * 100:.1f}%")
                rows.append({"run": name, "group": g, "passed": passed, "total": total})
        print(f"  classes passing all tests (as graded): {classes['all_passed']}/{classes['all_total']}")
        print(f"  classes passing all stated tests:      {classes['stated_passed']}/{classes['stated_total']}")
        rows.append({"run": name, "group": "classes_all_tests", "passed": classes["all_passed"], "total": classes["all_total"]})
        rows.append({"run": name, "group": "classes_stated_tests", "passed": classes["stated_passed"], "total": classes["stated_total"]})

    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["run", "group", "passed", "total"])
        writer.writeheader()
        writer.writerows(rows)
    print("\n->", OUT_CSV)


if __name__ == "__main__":
    main()
