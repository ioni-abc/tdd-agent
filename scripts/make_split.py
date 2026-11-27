"""Split each method's ClassEval tests into shown and hidden (held-out experiment).

For a method with n tests in methods_info[i]["test_code"]:
    n > shown     -> `shown` tests picked at random are shown, the other n - shown are hidden
    1 <= n <= shown -> n - 1 shown, 1 hidden (n = 1: 1 shown, 0 hidden, so the method still gets a test)
    n = 0         -> nothing (as for the TDD agent v1, the method gets no tests)
The pick is seeded per (seed, task_id, method), so the same seed always gives the same split.
Class-level tests (their class is in no methods_info[i]["test_class"]) are never shown and
not in the split.

The agent `tdd-heldout` gets only the shown tests. scripts/rescore_held_out.py grades every
run on the hidden tests only, so all agents are scored on tests none of them has seen.

From the project root:
    uv run python scripts/make_split.py                 # 2 shown per method, seed 0
    uv run python scripts/make_split.py --shown 3 --seed 1
Writes data/held_out_split.json:
    {task_id: {method_name: {"test_class": ..., "shown": [test names], "hidden": [test names]}}}
"""

import argparse
import json
import random

from tdd_agent import config
from tdd_agent.dataset import load_tasks, method_test_names


def split_names(names: list[str], shown: int, rng: random.Random) -> tuple[list[str], list[str]]:
    if not names:
        return [], []
    k = shown if len(names) > shown else max(1, len(names) - 1)
    picked = set(rng.sample(names, k))
    return [n for n in names if n in picked], [n for n in names if n not in picked]


def make_split(tasks: list[dict], shown: int, seed: int) -> dict:
    split = {}
    for task in tasks:
        per_method = {}
        for m in task["methods_info"]:
            rng = random.Random(f"{seed}:{task['task_id']}:{m['method_name']}")
            s, h = split_names(method_test_names(m["test_code"] or ""), shown, rng)
            per_method[m["method_name"]] = {"test_class": m["test_class"], "shown": s, "hidden": h}
        split[task["task_id"]] = per_method
    return split


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--shown", type=int, default=2, help="tests shown per method (default 2)")
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    split = make_split(load_tasks(), args.shown, args.seed)
    out = {"shown_per_method": args.shown, "seed": args.seed, "tasks": split}
    config.HELD_OUT_SPLIT_PATH.write_text(json.dumps(out, indent=1), encoding="utf-8")

    methods = [m for t in split.values() for m in t.values()]
    print(f"shown tests:  {sum(len(m['shown']) for m in methods)}")
    print(f"hidden tests: {sum(len(m['hidden']) for m in methods)}")
    print("->", config.HELD_OUT_SPLIT_PATH)


if __name__ == "__main__":
    main()
