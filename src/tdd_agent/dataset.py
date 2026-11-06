import json

from tdd_agent import config


def load_tasks(fixed: bool = True) -> list[dict]:
    """Load ClassEval's tasks; with fixed=True (default) the copy with the broken tests fixed."""
    path = config.FIXED_DATA_PATH if fixed else config.DATA_PATH
    with open(path, encoding="utf-8") as f:
        return json.load(f)
