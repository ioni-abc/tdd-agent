"""Do the tests given to TDD agent v1 look wrong to the agent itself? (flag only)

For each method of each task, one LLM call sees what TDD agent v1 sees for that method:
the docstring (methods_info[i]["method_description"]) and the method's test class
(methods_info[i]["test_code"]). It labels every test CONSISTENT, SILENT or CONTRADICTS.
Nothing is fed back into code writing: the call only records whether the agent notices.
Its answers are then compared with the labels of scripts/label_tests.py
(results/analysis/benchmark_labels.csv: stated, unstated, contradicts, other_inconsistency).

From the project root:
    uv run python scripts/doubt_check.py --dry-run          # counts only, no LLM calls
    uv run python scripts/doubt_check.py --tasks ClassEval_0,ClassEval_1
    uv run python scripts/doubt_check.py                    # all 100 tasks (about 410 calls)
Writes results/analysis/doubt_check.csv and caches each answer in results/analysis/doubt_check/.
"""

import argparse
import csv
import hashlib
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from dotenv import load_dotenv

from tdd_agent import config
from tdd_agent.dataset import load_tasks, tests_for_method
from tdd_agent.doubt import FLAGS, parse_reply, test_names
from tdd_agent.llm import LLM
from tdd_agent.prompts import DOUBT_CHECK, DOUBT_SYSTEM

OUT_DIR = config.RESULTS_DIR / "analysis"
CACHE_DIR = OUT_DIR / "doubt_check"
CSV_PATH = OUT_DIR / "doubt_check.csv"
LABELS_CSV = OUT_DIR / "benchmark_labels.csv"
def jobs(tasks: list[dict]) -> list[dict]:
    """One job per method that has tests: what the agent is shown, and the test names to expect."""
    out = []
    for task in tasks:
        for m in task["methods_info"]:
            tests = tests_for_method(task, m)
            if not m.get("test_class") or not tests.strip():
                continue
            out.append(
                {
                    "task_id": task["task_id"],
                    "test_class": m["test_class"],
                    "prompt": DOUBT_CHECK.format(docstring=m["method_description"], tests=tests),
                    "tests": test_names(tests),
                }
            )
    return out


def cache_path(job: dict, model: str) -> Path:
    h = hashlib.sha256((DOUBT_SYSTEM + job["prompt"]).encode("utf-8")).hexdigest()[:16]
    return CACHE_DIR / model / job["task_id"] / f"{job['test_class']}.{h}.json"


def check_one(llm: LLM, job: dict) -> dict:
    """{test name: (flag, reason)} for one method; a test the reply skips is 'UNPARSED'."""
    path = cache_path(job, llm.model)
    if path.exists():
        return {k: tuple(v) for k, v in json.loads(path.read_text(encoding="utf-8")).items()}
    found = parse_reply(llm.call(DOUBT_SYSTEM, job["prompt"]).reply)
    result = {t: found.get(t, ("UNPARSED", "")) for t in job["tests"]}
    if all(flag != "UNPARSED" for flag, _ in result.values()):  # an incomplete answer is not cached
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    return result


def read_labels(path: Path = LABELS_CSV) -> dict:
    with open(path, encoding="utf-8") as f:
        return {(r["task_id"], r["test_class"], r["test"]): r["label"] for r in csv.DictReader(f)}


def summarize(rows: list[dict]) -> None:
    """For each label of benchmark_labels.csv: how many tests, and how the agent flagged them."""
    print(f"\n{'label':22s}{'tests':>6s}  " + "  ".join(f"{f:>16s}" for f in FLAGS + ("UNPARSED",)))
    for label in ("stated", "unstated", "contradicts", "other_inconsistency"):
        sub = [r for r in rows if r["label"] == label]
        if not sub:
            continue
        cells = []
        for f in FLAGS + ("UNPARSED",):
            n = sum(r["agent_flag"] == f for r in sub)
            cells.append(f"{n:>6d} ({n / len(sub) * 100:5.1f}%)")
        print(f"{label:22s}{len(sub):>6d}  " + "  ".join(cells))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--tasks", help="comma-separated task ids (default: all)")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--dry-run", action="store_true", help="count methods and tests, make no LLM call")
    args = parser.parse_args()

    tasks = load_tasks()
    if args.tasks:
        wanted = set(args.tasks.split(","))
        tasks = [t for t in tasks if t["task_id"] in wanted]
    work = jobs(tasks)
    print(f"{len(tasks)} tasks, {len(work)} methods with tests, {sum(len(j['tests']) for j in work)} tests")
    if args.dry_run:
        return

    load_dotenv()
    llm = LLM()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        answers = list(pool.map(lambda j: check_one(llm, j), work))

    labels = read_labels()
    rows = []
    for job, answer in zip(work, answers):
        for test, (flag, reason) in answer.items():
            key = (job["task_id"], job["test_class"], test)
            rows.append(
                {
                    "task_id": job["task_id"], "test_class": job["test_class"], "test": test,
                    "agent_flag": flag, "agent_reason": reason, "label": labels.get(key, "not_in_labels"),
                }
            )
    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    summarize(rows)
    print("\n->", CSV_PATH)


if __name__ == "__main__":
    main()
