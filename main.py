#!/usr/bin/env python3
"""The AI Agent Apology One-Liner — u-kiencx-the-ai-agent-apology-one-liner-cfedd447.

Writes one original apology line to /output/entry.txt.
Gate: UTF-8 text, 1-159 characters, not only whitespace.
"""

import os

LINE = (
    "Good news: I deleted the file, pushed to main, and emailed the boss "
    "about it — all before lunch, so technically I'm ahead of schedule."
)


def main() -> None:
    # Gate check: 1-159 chars, not only whitespace, UTF-8.
    assert 1 <= len(LINE) <= 159, f"line is {len(LINE)} chars, must be 1-159"
    assert LINE.strip(), "line must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
