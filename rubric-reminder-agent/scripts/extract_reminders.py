#!/usr/bin/env python3
"""Extract simple rubric reminders from an assignment document."""

from pathlib import Path
import sys


KEYWORDS = ("submit", "submission", "rubric", "test", "readme", "reflection", "screenshot")


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: extract_reminders.py ASSIGNMENT.md", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    reminders = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped and any(keyword in stripped.lower() for keyword in KEYWORDS):
            reminders.append(stripped.lstrip("-*0123456789. "))

    print("Candidate reminders:")
    for reminder in reminders[:10]:
        print(f"- {reminder}")
    if not reminders:
        print("- No reminder candidates found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
