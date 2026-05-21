#!/usr/bin/env python3
"""Summarize course todo reminders."""

from pathlib import Path
import sys


KEYWORDS = ("todo", "deadline", "submit", "office hours", "follow up", "question")


def main() -> int:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "todo.md")
    text = path.read_text(encoding="utf-8")
    print(f"Reminder summary from {path}:")
    count = 0
    for line in text.splitlines():
        stripped = line.strip()
        if stripped and any(keyword in stripped.lower() for keyword in KEYWORDS):
            count += 1
            print(f"- {stripped.lstrip('-* ')}")
    if count == 0:
        print("- No reminder candidates found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
