"""Reading the agent's answer to the doubt check (shared by scripts/doubt_check.py and the tdd-doubt agent)."""

import ast
import re

FLAGS = ("CONSISTENT", "SILENT", "CONTRADICTS")
LINE = re.compile(r"^\W*(\w+)\W*:\s*(CONSISTENT|SILENT|CONTRADICTS)\b[\s\-–:]*(.*)$", re.IGNORECASE)


def test_names(test_code: str) -> list[str]:
    """The test methods of a method's test class, in file order."""
    cls = ast.parse(test_code).body[0]
    return [n.name for n in cls.body if isinstance(n, ast.FunctionDef) and n.name.startswith("test")]


def parse_reply(reply: str) -> dict:
    """'test_x: SILENT - reason' lines -> {test name: (flag, reason)}."""
    found = {}
    for line in reply.splitlines():
        m = LINE.match(line.strip())
        if m:
            found.setdefault(m.group(1), (m.group(2).upper(), m.group(3).strip()))
    return found
