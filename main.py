#!/usr/bin/env python3
"""Everyday Wonder entry.

Writes one sentence (at most 200 characters) about a small moment of
wonder in everyday life to /output/entry.txt. Deterministic: the same
sentence every run, no input, no network, no randomness.
"""

import os

SENTENCE = (
    "The fridge light came on at midnight and my leftover rice glowed "
    "like a small city that had stayed up waiting for me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
