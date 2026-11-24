#!/usr/bin/env python3
"""Write one loading-screen tip to the grader's output directory.

The tip is a single line of at most 200 characters, written for stressed
developers and the AI coding agents working beside them: sharp enough to
land mid-build, funny enough to make a tired developer feel seen.
"""

import os
import sys


TIP = (
    "Tip: your agent rewrote your function in 40 seconds, then spent "
    "20 minutes explaining why the old version was wrong. "
    "Trust the diff, not the essay."
)


def tip_line():
    """Return the tip as one clean line with no trailing newline."""
    return TIP.strip()


def validate_tip(text):
    """Check the tip against the gate: 1-200 chars, one line, not blank.

    Raises ValueError when the tip would fail the sealed scorer, so a
    bad tip never reaches the judge.
    """
    if not text or not text.strip():
        raise ValueError("tip must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("tip must be a single line")
    if len(text) > 200:
        raise ValueError("tip is %d characters, over the 200 limit" % len(text))
    return text


def main():
    line = validate_tip(tip_line())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
