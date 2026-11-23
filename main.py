#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

A robot vacuum writes its one-line excuse for missing a spot to
entry.txt. Deterministic: the same run always writes the same bytes.
Standard library only, no network. The line is a deadpan sensor log:
a timestamp, a map coordinate, a misidentified sock, and a vacuum
that refuses to admit its sensor was wrong.
"""

import os

LINE = (
    "Log 14:02 \u2014 spot at (3.1, 7.4) skipped. "
    "My obstacle sensor identified it as a small dog. "
    "It was a sock. I stand by the sensor."
)


def main() -> None:
    # The gate allows 1-200 UTF-8 characters; refuse to write anything else.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("entry line must be 1-200 non-blank characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
