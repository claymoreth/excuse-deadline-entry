#!/usr/bin/env python3
"""Write the excuse line to the output directory.

Output contract: exactly one file, entry.txt, containing exactly one
line (84 characters, em dash U+2014), no trailing newline, UTF-8.
"""

import os
import sys

LINE = "I didn't miss the deadline \u2014 I redefined it as a stretch goal, then missed that too."


def main() -> int:
    # Output contract: one file only (entry.txt), one line, no trailing
    # newline; MAKEFUN_BOT_DIR is unused here (no data files) but kept
    # as the repo-dir resolution pattern.
    bot_dir = os.environ.get("MAKEFUN_BOT_DIR") or os.getcwd()
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(LINE.encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
