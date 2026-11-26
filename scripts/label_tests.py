"""Label every test in task["test"] against the docstring of the method it tests.

Independent of any agent run: it asks only "is ClassEval's benchmark straight?".
For each test of each task, an LLM judge reads
  - the method's docstring       (task["methods_info"][i]["method_description"], what the agent sees)
  - the method's reference code  (task["methods_info"][i]["solution_code"])
  - the test's source            (from task["test"], plus its class's setUp)
and picks one label (LABELS below) plus a sentence MISSING: the general rule the docstring
should add so a programmer could implement what the test expects.

A test is mapped to its method through methods_info[i]["test_class"]. Tests whose class is in
no methods_info[i]["test_class"] (class-level tests, about 5%) have no docstring to compare
with; they are listed with label "no_method_info" and cost no LLM call.

From the project root:
    uv run python scripts/label_tests.py --dry-run                      # row counts only, no LLM calls
    uv run python scripts/label_tests.py --tasks ClassEval_1,ClassEval_4,ClassEval_92
    uv run python scripts/label_tests.py --sample 20 --seed 0           # 20 random tasks
    uv run python scripts/label_tests.py                                # all 100 tasks (about 2088 calls)
Writes results/analysis/benchmark_labels.csv and caches each answer in
results/analysis/benchmark_labels/, so a rerun makes no new calls (an unparsed answer is not cached).
"""

import argparse
import ast
import csv
import hashlib
import json
import random
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from dotenv import load_dotenv

from tdd_agent import config
from tdd_agent.dataset import load_tasks
from tdd_agent.llm import LLM

OUT_DIR = config.RESULTS_DIR / "analysis"
CACHE_DIR = OUT_DIR / "benchmark_labels"
CSV_PATH = OUT_DIR / "benchmark_labels.csv"

LABELS = {
    "stated": "the docstring states the behaviour this test checks, so a programmer following it would pass",
    "unstated": "the docstring does not say what this test expects (a convention, a format, an edge case), so a correct implementation could fail",
    "contradicts": "the docstring says something different from what the test (and the reference code) expect",
    "other_inconsistency": "the test and the docstring do not fit together, in a way that is neither unstated nor contradicts (say what the problem is, e.g. the test calls a different method than the one it is filed under)",
}

JUDGE_SYSTEM = """You check one unit test of a code-generation benchmark (ClassEval) against the docstring of the method it tests.
First decide, from the docstring alone, what a programmer would implement for the case the test covers.
Only then compare that with the test and the reference code.
Pick exactly one label from the list you are given.
Reply with exactly three lines:
LABEL: <one label>
REASON: <one sentence>
MISSING: <one sentence, or "none" if the label is stated>

Rules for MISSING:
- State the general rule the docstring should add, in words a programmer could implement.
- Do not copy this test's inputs, names, numbers or expected values.
- It must apply to every similar case, not only this test.
- For other_inconsistency, start REASON with a short name of the problem. MISSING is "none" unless the problem is a gap in the docstring."""

NO_METHOD = "no_method_info"


# ---------- step 1: list the tests and find each one's method ----------


def list_tests(task: dict) -> list[dict]:
    """Every test method in task["test"]: one dict per test, with its source (and its class's setUp)."""
    text = task["test"]
    tree = ast.parse(text)
    tests = []
    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        set_up = [
            ast.get_source_segment(text, n)
            for n in node.body
            if isinstance(n, ast.FunctionDef) and n.name == "setUp"
        ]
        for n in node.body:
            if isinstance(n, ast.FunctionDef) and n.name.startswith("test"):
                source = "\n\n".join(set_up + [ast.get_source_segment(text, n)])
                tests.append({"test_class": node.name, "test": n.name, "test_source": source})
    return tests


def build_rows(tasks: list[dict]) -> list[dict]:
    """One row per test in task["test"], joined with the method it belongs to (or none)."""
    rows = []
    for task in tasks:
        by_class = {m["test_class"]: m for m in task["methods_info"] if m.get("test_class")}
        for t in list_tests(task):
            m = by_class.get(t["test_class"])
            rows.append(
                {
                    "task_id": task["task_id"],
                    **t,
                    "method": m["method_name"] if m else "",
                    "docstring": m["method_description"] if m else "",
                    "solution": m["solution_code"] if m else "",
                }
            )
    return rows


# ---------- step 2: the prompt ----------


def judge_prompt(row: dict) -> str:
    labels = "\n".join(f"- {k}: {v}" for k, v in LABELS.items())
    return "\n\n".join(
        [
            f"Method: {row['method']}",
            f"Docstring of the method (what the agent sees):\n{row['docstring']}",
            f"Reference code of the method (solution_code):\n{row['solution']}",
            f"The test:\n{row['test_source']}",
            f"Labels:\n{labels}",
        ]
    )


# ---------- step 4: read the plain-line reply ----------


def parse_reply(reply: str) -> dict:
    """LABEL / REASON / MISSING lines -> dict. label is "unparsed" if it is not one of LABELS."""
    found = {}
    for line in reply.splitlines():
        key, sep, value = line.partition(":")
        if sep and key.strip().upper() in ("LABEL", "REASON", "MISSING"):
            found.setdefault(key.strip().lower(), value.strip())
    label = found.get("label", "").strip("`*\"' ").lower()
    return {
        "label": label if label in LABELS else "unparsed",
        "reason": found.get("reason", reply[:300]),
        "missing": found.get("missing", ""),
    }


# ---------- step 5: cache, calls, CSV ----------


def cache_path(row: dict, system: str, prompt: str) -> Path:
    """One file per test. The name carries a hash of system+prompt, so changing either one
    (the rules, the labels, the docstring, the test) misses the cache and asks again."""
    h = hashlib.sha256((system + prompt).encode("utf-8")).hexdigest()[:16]
    return CACHE_DIR / row["task_id"] / f"{row['test_class']}.{row['test']}.{h}.json"


def judge_one(llm: LLM, row: dict) -> dict:
    if not row["method"]:
        return {"label": NO_METHOD, "reason": "its test class is in no methods_info[i]['test_class']", "missing": ""}
    prompt = judge_prompt(row)
    path = cache_path(row, JUDGE_SYSTEM, prompt)
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    result = parse_reply(llm.call(JUDGE_SYSTEM, prompt).reply)
    if result["label"] != "unparsed":
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    return result


def run(rows: list[dict], llm: LLM, workers: int = 8) -> list[dict]:
    with ThreadPoolExecutor(max_workers=workers) as pool:
        results = list(pool.map(lambda r: judge_one(llm, r), rows))
    return [{**r, **res} for r, res in zip(rows, results)]


def write_csv(labelled: list[dict], path: Path = CSV_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    columns = ["task_id", "test_class", "test", "method", "label", "reason", "missing"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(labelled)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--tasks", help="comma-separated task ids, e.g. ClassEval_1,ClassEval_4 (default: all)")
    parser.add_argument("--sample", type=int, help="random sample of this many tasks (with --seed)")
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--dry-run", action="store_true", help="count rows, make no LLM call")
    args = parser.parse_args()

    tasks = load_tasks()
    if args.tasks:
        wanted = set(args.tasks.split(","))
        tasks = [t for t in tasks if t["task_id"] in wanted]
    if args.sample:
        tasks = random.Random(args.seed).sample(tasks, args.sample)
    rows = build_rows(tasks)
    to_judge = sum(1 for r in rows if r["method"])
    print(f"{len(tasks)} tasks, {len(rows)} tests, {to_judge} to judge, {len(rows) - to_judge} with no method")
    if args.dry_run:
        return

    load_dotenv()
    labelled = run(rows, LLM(), args.workers)
    write_csv(labelled)
    counts = {}
    for r in labelled:
        counts[r["label"]] = counts.get(r["label"], 0) + 1
    print(counts, "->", CSV_PATH)


if __name__ == "__main__":
    main()
