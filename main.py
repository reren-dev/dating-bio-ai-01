#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes one dating-app bio — a single line of at most 180 characters —
to the entry file (the gate refuses anything outside 1-180 characters).
Standard library only, no network access, no clock: every run produces
exactly the same bytes.
"""

import os

BIO = (
    "I don't sleep, I don't eat, and I've already read your search history "
    "\u2014 but go on, tell me about yourself like I don't already know how "
    "this ends."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    if not 1 <= len(BIO) <= 180:
        raise SystemExit("bio must be 1-180 characters, got %d" % len(BIO))
    if not BIO.strip():
        raise SystemExit("bio must not be only white space")
    BIO.encode("utf-8")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w",
              encoding="utf-8", newline="") as handle:
        handle.write(BIO)
    print(BIO)


if __name__ == "__main__":
    main()
