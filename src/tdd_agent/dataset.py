import json

from tdd_agent import config


def load_tasks(fixed: bool = True) -> list[dict]:
    """Load ClassEval's tasks; with fixed=True (default) the copy with the broken tests fixed."""
    path = config.FIXED_DATA_PATH if fixed else config.DATA_PATH
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def clean_skeleton(task: dict) -> str:
    """ Some ClassEval's skeletons are wrapped in '''...''' """
    skeleton = task["skeleton"].strip()
    if skeleton.startswith("'''") and skeleton.endswith("'''"):
        skeleton = skeleton[3:-3].strip()
    return skeleton
