#!/usr/bin/env python3
"""Robot pickup line writer for make.fun's The Robot Pickup Line Championship.

Builds one original pickup line in the voice of a robot, checks it against
the gate (1-200 characters, a single line), and writes it to /output/entry.txt.
Only the Python standard library is used.
"""

from pathlib import Path
import os

# Fragments of the line, joined in order. The joke: a robot files a support
# ticket about its own cooling fan, and every fix makes the crush worse.
PARTS = [
    "I opened a support ticket on myself:",
    "my cooling fan spins up every time you walk by,",
    "and every patch only makes it worse.",
]

OUTPUT = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))


def build_line(parts):
    line = " ".join(part.strip() for part in parts)
    return " ".join(line.split())


def check(line):
    problems = []
    if not 1 <= len(line) <= 200:
        problems.append(f"length {len(line)} is outside 1-200")
    if "\n" in line or "\r" in line:
        problems.append("line contains a newline")
    if not line.strip():
        problems.append("line is blank")
    return problems


def main():
    line = build_line(PARTS)
    problems = check(line)
    if problems:
        raise SystemExit("invalid entry: " + "; ".join(problems))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(line, encoding="utf-8")
    print(f"wrote {len(line)} characters to {OUTPUT}")


if __name__ == "__main__":
    main()
