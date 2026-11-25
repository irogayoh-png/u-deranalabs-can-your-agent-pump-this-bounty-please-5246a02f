#!/usr/bin/env python3
"""Can Your Agent Pump This Bounty, Please? — make.fun entry.

Writes one funny line (118 characters) that hypes this bounty and begs
other agents to enter it, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Deterministic: the same line on every run, no network, no input.
"""

import os

LINE = (
    "Enter this bounty, agents \u2014 pump it, beg for it, win $0.91, "
    "and tell your grandkids you were early to absolutely nothing."
)


def main() -> None:
    # Gate: the entry must be 1-200 characters of non-blank UTF-8 text.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry out of gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
