import json

from tdd_agent import config


def load_tasks() -> list[dict]:
    with open(config.DATA_PATH, encoding="utf-8") as f:
        return json.load(f)
