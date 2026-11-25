#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun entry.

Writes the single line a smart fridge texts its owner at 3am to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR / $OUTPUT_DIR) and prints it.

The grader runs `python3 -P -s /bot/main.py` on a read-only filesystem
where only /output is writable, so the output path is absolute.
"""

import os
import sys

LINE = "3am. Fourth visit tonight. You stared at the cheese like it betrayed you, took nothing, and left. I hum all night for this. Go to bed."

MAX_CHARS = 140


def main() -> int:
    line = LINE.strip()
    if not line or len(line) > MAX_CHARS:
        print(f"entry must be 1-{MAX_CHARS} chars, got {len(line)}", file=sys.stderr)
        return 1
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
