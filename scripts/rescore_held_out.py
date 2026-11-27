"""Re-score runs on the hidden tests of data/held_out_split.json only.

No agent has seen a hidden test: the baseline and tdd-own never see any of task["test"], and
tdd-heldout sees only the shown ones. So on hidden tests the comparison is fair.
tdd (TDD agent v1) saw all of them; it is included as the "graded on what it saw" reference.

For each run it reports, over the hidden tests only:
  - pass rate per label (labels from results/analysis/benchmark_labels.csv)
  - classes passing all their hidden `stated` tests (classes without one are left out)

From the project root (after make_split.py and grading the tdd-heldout run):
    uv run python scripts/rescore_held_out.py --runs baseline_2026-11-19T14-38-59,tdd-own_2026-11-19T14-38-57,tdd_2026-11-19T14-38-58,<tdd-heldout run>
Writes results/analysis/rescore_held_out.csv (one row per run and group).
"""

import argparse
import csv
import json
from collections import Counter, defaultdict

from rescore_stated import ANALYSIS, LABELS_CSV, RUNS, read_labels, run_results

from tdd_agent import config

OUT_CSV = ANALYSIS / "rescore_held_out.csv"
GROUPS = ["stated", "unstated", "contradicts", "other_inconsistency"]


def hidden_keys(split: dict) -> set:
    """(task_id, test class, test) of every hidden test."""
    return {
        (task_id, m["test_class"], test)
        for task_id, methods in split["tasks"].items()
        for m in methods.values()
        for test in m["hidden"]
    }


def score(results: dict, labels: dict, hidden: set) -> tuple[dict, dict, int]:
    by_group = defaultdict(lambda: [0, 0])
    stated_ok, stated_n = defaultdict(lambda: True), Counter()
    missing = 0
    for key in hidden:
        if key not in results:  # e.g. the code crashed before this test ran: count it as failed
            missing += 1
        ok = results.get(key, False)
        label = labels.get(key, "unlabelled")
        by_group[label][0] += ok
        by_group[label][1] += 1
        if label == "stated":
            stated_n[key[0]] += 1
            stated_ok[key[0]] &= ok
    classes = {"passed": sum(stated_ok[t] for t in stated_n), "total": len(stated_n)}
    return by_group, classes, missing


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--runs", help="comma-separated run folder names (default: baseline, tdd, tdd-own)")
    args = parser.parse_args()

    split = json.loads(config.HELD_OUT_SPLIT_PATH.read_text(encoding="utf-8"))
    hidden = hidden_keys(split)
    labels = read_labels(LABELS_CSV)
    runs = args.runs.split(",") if args.runs else RUNS
    print(f"split: {split['shown_per_method']} shown per method, seed {split['seed']}, {len(hidden)} hidden tests")

    rows = []
    for name in runs:
        results = run_results(config.RESULTS_DIR / "experiments" / name)
        by_group, classes, missing = score(results, labels, hidden)
        print(f"\n{name}" + (f"  ({missing} hidden tests not in the log, counted as failed)" if missing else ""))
        for g in GROUPS + ["unlabelled"]:
            passed, total = by_group[g]
            if total:
                print(f"  {g:20s} {passed}/{total} = {passed / total * 100:.1f}%")
                rows.append({"run": name, "group": g, "passed": passed, "total": total})
        print(f"  classes passing all hidden stated tests: {classes['passed']}/{classes['total']}")
        rows.append({"run": name, "group": "classes_hidden_stated", **classes})

    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["run", "group", "passed", "total"])
        writer.writeheader()
        writer.writerows(rows)
    print("\n->", OUT_CSV)


if __name__ == "__main__":
    main()
