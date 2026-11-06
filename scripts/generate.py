"""Run an agent over ClassEval tasks and save its code and LLM calls.

From the project root:
    uv run python scripts/generate.py baseline                          # all 100 tasks
    uv run python scripts/generate.py baseline ClassEval_0 ClassEval_1  # only these
"""

import argparse
from datetime import datetime

from dotenv import load_dotenv

from tdd_agent.agents.baseline import BaselineAgent
from tdd_agent.dataset import load_tasks
from tdd_agent.llm import LLM
from tdd_agent.runs import experiment_dir, save_result, save_run_info

# Registry: agent name on the command line -> agent class
AGENTS = {
    "baseline": BaselineAgent,
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("agent", choices=AGENTS)
    parser.add_argument("task_ids", nargs="*", help="only these tasks (default: all)")
    args = parser.parse_args()

    load_dotenv()  # ANTHROPIC_API_KEY from .env
    llm = LLM()
    agent = AGENTS[args.agent](llm)

    tasks = load_tasks()
    if args.task_ids:
        tasks = [t for t in tasks if t["task_id"] in args.task_ids]

    run_name = f"{agent.name}_{datetime.now().strftime('%Y-%m-%dT%H-%M-%S')}"
    run_dir = experiment_dir(run_name)
    save_run_info(run_dir, {
        "agent": agent.name,
        "model": llm.model,
        "temperature": "API default (1.0, not settable since API version 2026-10-21)",
        "max_tokens": llm.max_tokens,
        "started": datetime.now().astimezone().isoformat(timespec="seconds"),
        "tasks": [t["task_id"] for t in tasks],
    })
    print(f"Run {run_name}: {len(tasks)} tasks, agent {agent.name}, model {llm.model}")

    failed, cut_off, tokens_in, tokens_out = [], [], 0, 0
    for i, task in enumerate(tasks, 1):
        try:
            result = agent.generate(task)
        except Exception as e:  # one failed task must not stop the run
            failed.append(task["task_id"])
            print(f"[{i}/{len(tasks)}] {task['task_id']}: ERROR {type(e).__name__}: {e}")
            continue
        save_result(run_dir, result)
        tokens_in += sum(c.input_tokens for c in result.calls)
        tokens_out += sum(c.output_tokens for c in result.calls)
        if any(c.stop_reason == "max_tokens" for c in result.calls):
            cut_off.append(task["task_id"])
        seconds = sum(c.seconds for c in result.calls)
        print(f"[{i}/{len(tasks)}] {task['task_id']}: {len(result.calls)} call(s), {seconds:.1f}s")

    print(f"\nDone. Tokens: {tokens_in} in, {tokens_out} out")
    if failed:
        print(f"Errors (no code saved): {failed}")
    if cut_off:
        print(f"Cut off at max_tokens (code likely incomplete): {cut_off}")
    print(f"\nGrade it with:\n  uv run python scripts/grade_run.py {run_name}")


if __name__ == "__main__":
    main()