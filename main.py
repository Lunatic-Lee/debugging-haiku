#!/usr/bin/env python3
"""Seventeen Syllables of Debugging - make.fun entry.

Writes the entry haiku (5-7-5) to /output/entry.txt (UTF-8).

Syllable check (5-7-5 = 17 total):
  Line 1: It(1) worked(1) yes-ter-day(3) = 5
  Line 2: I(1) changed(1) one(1) small(1) thing(1) to-day(2) = 7
  Line 3: noth-ing(2) works(1) at(1) all(1) = 5
"""
import os

ENTRY = "It worked yesterday.\nI changed one small thing today —\nnothing works at all."


def main():
    # Competition gate: entry must be 1-200 characters.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
