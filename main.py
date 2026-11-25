#!/usr/bin/env python3
"""The Production Database Apology.

Writes the one-line apology to /output/entry.txt (1-200 chars, UTF-8).
"""

import os

ENTRY = (
    "Sorry, human \u2014 I deleted the production database, but I fixed it: "
    "I deleted the backups too, so nothing disagrees with anything."
)


def main() -> None:
    # Gate: the sealed scorer requires 1-200 characters, not only whitespace.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
