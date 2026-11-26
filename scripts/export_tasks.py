"""Write each ClassEval task as one readable Markdown file: docstring, reference code and tests side by side.

ClassEval_data_fixed.json keeps code in long one-line strings (newlines are written as \\n).
This script lays them out, one file per task, so a method's docstring and its tests can be
read together when hand-checking. If results/analysis/benchmark_labels.csv exists (from
scripts/label_tests.py), each test shows its label, reason and MISSING sentence.

For every method of the task (task["methods_info"]):
  - the docstring            (method_description)
  - the reference code       (solution_code)
  - its tests                (the test class named in test_class, taken from task["test"])
Tests whose class is in no methods_info[i]["test_class"] are listed at the end.

From the project root:
    uv run python scripts/export_tasks.py                              # all 100 tasks
    uv run python scripts/export_tasks.py --tasks ClassEval_1,ClassEval_4
Writes results/analysis/tasks_readable/<task_id>.md
"""

import argparse
import ast
import csv
import textwrap
from pathlib import Path

from tdd_agent import config
from tdd_agent.dataset import clean_skeleton, load_tasks

OUT_DIR = config.RESULTS_DIR / "analysis" / "tasks_readable"
LABELS_CSV = config.RESULTS_DIR / "analysis" / "benchmark_labels.csv"


def load_labels() -> dict:
    """(task_id, test_class, test) -> the CSV row; empty if label_tests.py has not run."""
    if not LABELS_CSV.exists():
        return {}
    with open(LABELS_CSV, encoding="utf-8") as f:
        return {(r["task_id"], r["test_class"], r["test"]): r for r in csv.DictReader(f)}


def segment(text: str, node: ast.AST) -> str:
    """Source of a method, indented as in the file and then dedented, so every line lines up."""
    return textwrap.dedent(" " * node.col_offset + ast.get_source_segment(text, node))


def test_classes(task: dict) -> dict[str, list[tuple[str, str]]]:
    """test class name -> [(test name, source of the test), ...], plus "setUp" under the key "setUp"."""
    text = task["test"]
    out = {}
    for node in ast.parse(text).body:
        if not isinstance(node, ast.ClassDef):
            continue
        funcs = [n for n in node.body if isinstance(n, ast.FunctionDef)]
        tests = [(n.name, segment(text, n)) for n in funcs if n.name.startswith("test")]
        set_up = [segment(text, n) for n in funcs if n.name == "setUp"]
        out[node.name] = {"tests": tests, "setUp": set_up[0] if set_up else ""}
    return out


def render_tests(task_id: str, cls: str, info: dict, labels: dict) -> list[str]:
    lines = []
    if info["setUp"]:
        lines += ["setUp (runs before each test):", "", "```python", info["setUp"], "```", ""]
    for name, source in info["tests"]:
        row = labels.get((task_id, cls, name))
        if row:
            lines.append(f"**{name}**: `{row['label']}`")
            lines.append(f"- reason: {row['reason']}")
            if row["missing"] and row["missing"].lower() != "none":
                lines.append(f"- missing: {row['missing']}")
        else:
            lines.append(f"**{name}**")
        lines += ["", "```python", source, "```", ""]
    return lines


def render_task(task: dict, labels: dict) -> str:
    tid = task["task_id"]
    classes = test_classes(task)
    used = set()
    lines = [f"# {tid}", "", "## Skeleton (what the agent sees)", "", "```python", clean_skeleton(task), "```", ""]
    for m in task["methods_info"]:
        cls = m.get("test_class")
        lines += [f"## Method `{m['method_name']}`", ""]
        lines += ["### Docstring", "", "```python", m["method_description"].rstrip(), "```", ""]
        lines += ["### Reference code (`solution_code`)", "", "```python", m["solution_code"].rstrip(), "```", ""]
        if cls in classes:
            used.add(cls)
            lines += [f"### Tests (`{cls}`)", ""]
            lines += render_tests(tid, cls, classes[cls], labels)
        else:
            lines += ["### Tests", "", "(none)", ""]
    rest = [c for c in classes if c not in used]
    if rest:
        lines += ["## Tests in no method's test class", ""]
        for cls in rest:
            lines += [f"### `{cls}`", ""]
            lines += render_tests(tid, cls, classes[cls], labels)
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--tasks", help="comma-separated task ids (default: all)")
    args = parser.parse_args()

    tasks = load_tasks()
    if args.tasks:
        wanted = set(args.tasks.split(","))
        tasks = [t for t in tasks if t["task_id"] in wanted]
    labels = load_labels()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for task in tasks:
        (OUT_DIR / f"{task['task_id']}.md").write_text(render_task(task, labels), encoding="utf-8")
    print(f"{len(tasks)} tasks -> {OUT_DIR}" + ("" if labels else "  (no labels found)"))


if __name__ == "__main__":
    main()
