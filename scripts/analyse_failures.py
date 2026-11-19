"""Give every failing test of a TDD run one reason, then count the reasons.

Two kinds of failing test (see the code x tests matrix):
  - agent_test:     a test in tests/<task>.py that fails on task["solution_code"]   (from tests_on_solution/)
  - classeval_test: a test in task["test"] that fails on code/<task>.py           (from grades/, failed classes only)

Reasons found automatically, without an LLM:
  - no_tests_ran            (class) grades/ shows 0 tests ran: the file has a SyntaxError
  - module_failed_to_load   (class) the file could not be imported, e.g. a missing module
  - no_method_info          (classeval_test) its test class is in no methods_info[i]["test_class"]
  - broken_test_code        (agent_test) ERROR with AttributeError / NameError / TypeError
  - docstring_example_wrong (agent_test) the test repeats a >>> example of the method's docstring
                            that task["solution_code"] does not reproduce
The rest is judged by an LLM (one call per test, labels in LABELS below).
Docstring examples are run with doctest against task["solution_code"], for all 100 tasks
(saved to results/analysis/docstring_examples.json: a benchmark finding of its own).

From the project root (after grade_run.py and grade_tests.py on the run):
    uv run python scripts/analyse_failures.py tdd-own_2026-11-19T14-38-57
    uv run python scripts/analyse_failures.py tdd-own_2026-11-19T14-38-57 --no-llm   # automatic part only
Writes <run>/analysis/failures.csv (one row per failing test), <run>/analysis/summary.json,
and caches each LLM answer in <run>/analysis/llm/ so a rerun makes no new calls.
"""

import argparse
import ast
import csv
import inspect
import json
import re
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from dotenv import load_dotenv

from tdd_agent import config
from tdd_agent.dataset import load_tasks
from tdd_agent.llm import LLM
from tdd_agent.runs import experiment_dir

HEADER = re.compile(r"^(FAIL|ERROR): (\w+) \(temp_file\.(\w+)\.\w+\)", re.MULTILINE)
SEPARATOR = "=" * 70
BROKEN_TEST_ERRORS = ("AttributeError", "NameError", "TypeError")

# ---------- reading the logs ----------


def failures_in_log(log: str) -> list[dict]:
    """One dict per FAIL/ERROR block of a unittest log: status, test, test_class, error line."""
    blocks = log.split(SEPARATOR)[1:]
    out = []
    for block in blocks:
        m = HEADER.search(block)
        if not m:
            continue
        lines = [
            line
            for line in block.splitlines()
            if re.match(r"^\w*(Error|Exception)\b", line)
        ]
        out.append(
            {
                "status": m.group(1),
                "test": m.group(2),
                "test_class": m.group(3),
                "error": lines[-1] if lines else "",
            }
        )
    return out


def test_source(file_text: str, test_class: str, test: str) -> str:
    """The source of one test method (plus its class's setUp, which often matters)."""
    try:
        tree = ast.parse(file_text)
    except SyntaxError:
        return ""
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == test_class:
            parts = [
                ast.get_source_segment(file_text, n)
                for n in node.body
                if isinstance(n, ast.FunctionDef) and n.name in ("setUp", test)
            ]
            return "\n\n".join(p for p in parts if p)
    return ""


def method_source(code: str, method: str) -> str:
    """The source of one method of the (only) class in a file, or "" if it can't be found."""
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return ""
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == method:
            return ast.get_source_segment(code, node) or ""
    return ""


# ---------- docstring examples vs task["solution_code"] ----------

DOCTEST_HARNESS = """
import doctest, json
_FAILS = []
class _Runner(doctest.DocTestRunner):
    def report_failure(self, out, test, example, got):
        _FAILS.append({"source": example.source.strip(), "want": example.want.strip(), "got": got.strip()})
    def report_unexpected_exception(self, out, test, example, exc_info):
        _FAILS.append({"source": example.source.strip(), "want": example.want.strip(), "got": repr(exc_info[1])})
_TEST = doctest.DocTestParser().get_doctest(_DOCSTRING, dict(globals()), "m", None, 0)
_Runner(verbose=False).run(_TEST, out=lambda s: None)
print("@@DOCTEST@@" + json.dumps({"attempted": len(_TEST.examples), "failed": _FAILS}))
"""


def docstring_examples(task: dict, method: dict) -> dict:
    """Run the >>> examples of one method's docstring against task["solution_code"], in a subprocess."""
    m = re.search(r'"""(.*?)"""', method["method_description"], re.DOTALL)
    docstring = inspect.cleandoc(m.group(1)) if m else ""
    if ">>>" not in docstring:
        return {"attempted": 0, "failed": []}
    script = (
        task["solution_code"]
        + "\n\n_DOCSTRING = "
        + repr(docstring)
        + "\n"
        + DOCTEST_HARNESS
    )
    with tempfile.TemporaryDirectory() as tmp:
        (Path(tmp) / "doc.py").write_text(script, encoding="utf-8")
        try:
            res = subprocess.run(
                [sys.executable, "doc.py"],
                cwd=tmp,
                capture_output=True,
                text=True,
                timeout=10,
            )
        except subprocess.TimeoutExpired:
            return {"attempted": 0, "failed": [], "note": "timeout"}
    for line in res.stdout.splitlines():
        if line.startswith("@@DOCTEST@@"):
            result = json.loads(line[len("@@DOCTEST@@") :])
            for f in result["failed"]:
                f["contradicts"] = contradicts(f["want"], f["got"])
            return result
    return {
        "attempted": 0,
        "failed": [],
        "note": "did not run: " + res.stderr.strip()[-200:],
    }


def contradicts(want: str, got: str) -> bool:
    """A real contradiction: the docstring's expected value and solution_code's value are both
    plain Python values (numbers, strings, lists, dicts...) and they are not equal.

    Not counted: examples that crash (often the docstring never creates the object it uses),
    pseudo-code notes like "account1.balance = 700", and differences in spelling only
    (["John"] vs ['John'], 3.00 vs 3.0), which compare equal as values.
    """
    try:
        return ast.literal_eval(want) != ast.literal_eval(got)
    except (ValueError, SyntaxError, TypeError, MemoryError, RecursionError):
        return False


def all_docstring_examples(tasks: list[dict]) -> dict:
    """task_id -> method_name -> doctest result, for every method of every task (cached on disk)."""
    path = config.RESULTS_DIR / "analysis" / "docstring_examples.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    result = {
        t["task_id"]: {
            m["method_name"]: docstring_examples(t, m) for m in t["methods_info"]
        }
        for t in tasks
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    return result


def call_part(source: str) -> str:
    """'obj.find_longest_word('I am a student.')' -> ".find_longest_word('I am a student.')", spaces removed."""
    i = source.find(".")
    return re.sub(r"\s", "", source[i:] if i >= 0 else source)


# ---------- the LLM judge ----------

LABELS = {
    "agent_test": {
        "docstring_contradicts_solution": "the test follows what the docstring says (text or example), but solution_code does otherwise",
        "agent_misread_docstring": "the docstring states the behaviour clearly, matching solution_code, and the test expects something else",
        "agent_assumed_unstated": "the docstring does not describe the behaviour the test checks; the agent assumed it",
        "broken_test_code": "the test itself is faulty code (wrong API use, calls something that does not exist)",
    },
    "classeval_test": {
        "caused_by_wrong_agent_test": "one of the agent's own wrong tests (listed) made the code behave the way that fails here",
        "docstring_contradicts_solution": "the agent's code follows the docstring (text or example), but solution_code and this test expect otherwise",
        "stated_but_untested": "the docstring states the behaviour; the agent's code gets it wrong and none of its tests checked it",
        "unstated_behaviour": "the docstring does not describe the behaviour this test checks",
        "other_code_bug": "any other mistake in the agent's code",
    },
}

JUDGE_SYSTEM = """You analyse why a unit test fails in a code-generation benchmark (ClassEval).
An agent read a class skeleton (docstrings only), wrote its own tests, then code that passes them.
Pick exactly one label from the list you are given. Judge only from the material shown.
Reply with only a JSON object: {"label": "<one label>", "reason": "<one sentence>"}"""


def judge_prompt(kind: str, item: dict) -> str:
    labels = "\n".join(f"- {k}: {v}" for k, v in LABELS[kind].items())
    parts = [
        f"Kind of failing test: {kind}",
        "agent_test = a test the agent wrote, failing on ClassEval's reference solution."
        if kind == "agent_test"
        else "classeval_test = a ClassEval test, failing on the agent's code.",
        f"Method: {item['method']}",
        f"Docstring of the method (what the agent saw):\n{item['docstring']}",
        f"Reference solution of the method (solution_code):\n{item['solution']}",
        f"The failing test:\n{item['test_source']}",
        f"Error when it ran:\n{item['error']}",
    ]
    if kind == "classeval_test":
        parts.append(
            f"The agent's code for the method:\n{item['agent_method'] or '(not found)'}"
        )
        parts.append(
            f"The agent's wrong tests for this method (they fail on the reference solution):\n{item['wrong_agent_tests'] or '(none)'}"
        )
    parts.append(f"Labels:\n{labels}")
    return "\n\n".join(parts)


def judge(llm: LLM, kind: str, item: dict, cache: Path) -> dict:
    if cache.exists():
        return json.loads(cache.read_text(encoding="utf-8"))
    call = llm.call(JUDGE_SYSTEM, judge_prompt(kind, item))
    m = re.search(r"\{.*\}", call.reply, re.DOTALL)
    try:
        answer = json.loads(m.group(0)) if m else {}
    except json.JSONDecodeError:
        answer = {}
    label = answer.get("label")
    result = {
        "label": label if label in LABELS[kind] else "unparsed",
        "reason": answer.get("reason", call.reply[:300]),
    }
    if (
        result["label"] != "unparsed"
    ):  # an unusable answer is not cached, so a rerun asks again
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(json.dumps(result, indent=2), encoding="utf-8")
    return result


# ---------- building the rows ----------


def collect(run_dir: Path, tasks: dict, doc: dict) -> list[dict]:
    rows = []
    for grade_path in sorted(
        (run_dir / "grades").glob("*.json"), key=lambda p: int(p.stem.split("_")[1])
    ):
        grade = json.loads(grade_path.read_text(encoding="utf-8"))
        tid = grade["task_id"]
        task = tasks[tid]
        by_name = {m["method_name"]: m for m in task["methods_info"]}
        class_to_method = {
            m["test_class"]: m["method_name"] for m in task["methods_info"]
        }
        suite_path, code_path = (
            run_dir / "tests" / f"{tid}.py",
            run_dir / "code" / f"{tid}.py",
        )
        suite = suite_path.read_text(encoding="utf-8") if suite_path.exists() else ""
        code = code_path.read_text(encoding="utf-8")

        def base(kind, f, method):
            m = by_name.get(method)
            return {
                "task_id": tid,
                "class_passed": grade["class_passed"],
                "kind": kind,
                "test": f["test"],
                "test_class": f["test_class"],
                "method": method or "",
                "status": f["status"],
                "error": f["error"],
                "docstring": m["method_description"] if m else "",
                "solution": m["solution_code"] if m else "",
            }

        # agent tests that fail on task["solution_code"] (all tasks: a wrong test is wrong even in a passing class)
        wrong_by_method = defaultdict(list)
        ref_path = run_dir / "tests_on_solution" / grade_path.name
        if ref_path.exists():
            for f in failures_in_log(
                json.loads(ref_path.read_text(encoding="utf-8"))["log"]
            ):
                method = f["test_class"].removeprefix("AgentTest_")
                row = base("agent_test", f, method)
                row["test_source"] = test_source(suite, f["test_class"], f["test"])
                if f["status"] == "ERROR" and f["error"].startswith(BROKEN_TEST_ERRORS):
                    row["reason"], row["by"] = "broken_test_code", "rule"
                else:
                    fails = [
                        x
                        for x in doc.get(tid, {}).get(method, {}).get("failed", [])
                        if x["contradicts"]
                    ]
                    body = re.sub(r"\s", "", row["test_source"])
                    if any(
                        call_part(x["source"]) in body
                        for x in fails
                        if "." in x["source"]
                    ):
                        row["reason"], row["by"] = "docstring_example_wrong", "rule"
                rows.append(row)
                wrong_by_method[method].append(row["test_source"])

        if grade["class_passed"]:
            continue
        whole = None
        if (
            grade["counts"]["tests_total"] == 0
        ):  # the file did not even get to run tests (e.g. a SyntaxError)
            whole = (
                "no_tests_ran",
                grade["log"].strip().splitlines()[-1] if grade["log"].strip() else "",
            )
        elif (
            "_FailedTest" in grade["log"]
        ):  # the file ran but could not be imported (e.g. a missing module)
            errs = [
                line
                for line in grade["log"].splitlines()
                if re.match(r"^\w*(Error|Exception)\b", line)
            ]
            whole = ("module_failed_to_load", errs[-1] if errs else "")
        if whole:
            rows.append(
                {
                    "task_id": tid,
                    "class_passed": False,
                    "kind": "class",
                    "test": "",
                    "test_class": "",
                    "method": "",
                    "status": "",
                    "error": whole[1],
                    "reason": whole[0],
                    "by": "rule",
                }
            )
            continue
        # ClassEval tests that fail on code/<task>.py
        for f in failures_in_log(grade["log"]):
            method = class_to_method.get(f["test_class"])
            row = base("classeval_test", f, method)
            row["test_source"] = test_source(task["test"], f["test_class"], f["test"])
            if method is None:
                row["reason"], row["by"] = "no_method_info", "rule"
            else:
                row["agent_method"] = method_source(code, method)
                row["wrong_agent_tests"] = "\n\n".join(wrong_by_method.get(method, []))
            rows.append(row)
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_name")
    parser.add_argument(
        "--no-llm", action="store_true", help="only the automatic reasons"
    )
    parser.add_argument("--workers", type=int, default=8, help="parallel LLM calls")
    args = parser.parse_args()

    run_dir = experiment_dir(args.run_name)
    if not (run_dir / "grades").is_dir():
        parser.error(f"grade the run first: no grades/ in {run_dir}")
    tasks_list = load_tasks()
    tasks = {t["task_id"]: t for t in tasks_list}

    print(
        "Running docstring examples against solution_code (all tasks, cached after the first run)..."
    )
    doc = all_docstring_examples(tasks_list)
    rows = collect(run_dir, tasks, doc)

    todo = [r for r in rows if "reason" not in r]
    if args.no_llm:
        for r in todo:
            r["reason"], r["by"] = "needs_judgment", "none"
    else:
        load_dotenv()
        llm = LLM()
        out = run_dir / "analysis" / "llm"

        def work(r):
            return judge(
                llm,
                r["kind"],
                r,
                out
                / f"{r['task_id']}__{r['kind']}__{r['test_class']}__{r['test']}.json",
            )

        print(
            f"Judging {len(todo)} tests with {llm.model} ({args.workers} in parallel)..."
        )
        with ThreadPoolExecutor(args.workers) as pool:
            for r, verdict in zip(todo, pool.map(work, todo)):
                r["reason"], r["by"], r["llm_reason"] = (
                    verdict["label"],
                    "llm",
                    verdict["reason"],
                )

    # ---------- write ----------
    adir = run_dir / "analysis"
    adir.mkdir(parents=True, exist_ok=True)
    cols = [
        "task_id",
        "class_passed",
        "kind",
        "method",
        "test_class",
        "test",
        "status",
        "error",
        "reason",
        "by",
        "llm_reason",
    ]
    with open(adir / "failures.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    failed_classes = sorted(
        {r["task_id"] for r in rows if not r["class_passed"]},
        key=lambda t: int(t.split("_")[1]),
    )
    per_class = defaultdict(Counter)
    for r in rows:
        if r["kind"] != "agent_test" or not r["class_passed"]:
            per_class[r["task_id"]][(r["kind"], r["reason"])] += 1
    summary = {
        "run": args.run_name,
        "failed_classes": len(failed_classes),
        "tests_by_reason": {
            kind: dict(
                Counter(r["reason"] for r in rows if r["kind"] == kind).most_common()
            )
            for kind in ("class", "classeval_test", "agent_test")
        },
        "agent_tests_in_passing_classes": sum(
            1 for r in rows if r["kind"] == "agent_test" and r["class_passed"]
        ),
        "classes_by_classeval_reason": dict(
            Counter(
                reason
                for tid in failed_classes
                for reason in {
                    r["reason"]
                    for r in rows
                    if r["task_id"] == tid and r["kind"] in ("classeval_test", "class")
                }
            ).most_common()
        ),
        "docstring_examples": {
            "methods_with_examples": sum(
                1 for t in doc.values() for v in t.values() if v.get("attempted")
            ),
            "examples": sum(
                v.get("attempted", 0) for t in doc.values() for v in t.values()
            ),
            "examples_not_reproduced_by_solution_code": sum(
                len(v.get("failed", [])) for t in doc.values() for v in t.values()
            ),
            "examples_contradicting_solution_code": sum(
                1
                for t in doc.values()
                for v in t.values()
                for f in v.get("failed", [])
                if f["contradicts"]
            ),
            "tasks_with_a_contradicting_example": sum(
                1
                for t in doc.values()
                if any(
                    f["contradicts"] for v in t.values() for f in v.get("failed", [])
                )
            ),
        },
    }
    (adir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print(f"\n======= {args.run_name.upper()}: WHY TESTS FAIL =======")
    print(f"{len(failed_classes)} failed classes\n")
    for kind, title in [
        (
            "classeval_test",
            "ClassEval tests failing on the agent's code (task['test'] vs code/)",
        ),
        (
            "agent_test",
            "Agent tests failing on solution_code (tests/ vs task['solution_code'])",
        ),
        ("class", "Classes where the test file could not run"),
    ]:
        counts = summary["tests_by_reason"][kind]
        if counts:
            print(f"{title}: {sum(counts.values())}")
            for reason, n in counts.items():
                print(f"  {n:4d}  {reason}")
            print()
    print("Failed classes per reason (a class with several reasons counts under each):")
    for reason, n in summary["classes_by_classeval_reason"].items():
        print(f"  {n:4d}  {reason}")
    d = summary["docstring_examples"]
    print(
        f"\nBenchmark: {d['examples_contradicting_solution_code']} of {d['examples']} docstring examples give a "
        f"different value on solution_code, in {d['tasks_with_a_contradicting_example']} of 100 tasks "
        f"({d['examples_not_reproduced_by_solution_code']} don't reproduce at all, most because they can't run)"
    )
    print(f"\nPer test: {adir / 'failures.csv'}")


if __name__ == "__main__":
    main()
