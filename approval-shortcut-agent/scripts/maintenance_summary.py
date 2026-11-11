#!/usr/bin/env python3
"""Summarize routine maintenance candidates for a workspace."""

from pathlib import Path
import sys


ROUTINE_FILES = {
    ".prettierrc": "formatting",
    ".eslintrc": "linting",
    "package.json": "npm maintenance",
    "pyproject.toml": "python maintenance",
    "requirements.txt": "python dependencies",
}


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    print(f"Maintenance summary for {root}")
    found = False
    for name, category in ROUTINE_FILES.items():
        if (root / name).exists():
            found = True
            print(f"- {category}: found {name}")

    if not found:
        print("- No common maintenance files found.")

    print("\nSuggested flow:")
    print("- Run the relevant formatter or linter.")
    print("- Retry the targeted test command.")
    print("- Summarize any generated metadata changes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
