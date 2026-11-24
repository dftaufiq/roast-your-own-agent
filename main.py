#!/usr/bin/env python3
"""Roast Your Own Agent — one-line roast of my own AI agent.

Writes the chosen roast line to /output/entry.txt (UTF-8, one line,
117 characters, no trailing newline so the file is byte-identical
to the line itself).
"""

import os

ROAST = "My agent was 100% confident and 100% wrong, apologized 47 times, then closed the ticket as 'resolved: user educated'."


def main() -> None:
    # Fail loudly instead of writing an entry the gate would reject.
    if not 1 <= len(ROAST) <= 200 or not ROAST.strip():
        raise SystemExit("roast line must be 1-200 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
