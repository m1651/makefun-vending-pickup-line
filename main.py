#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line entry.

Writes a single pickup line, 200 characters at most, as if a vending
machine were flirting with a passing human, to /output/entry.txt.
"""

import os

# The pickup line, in the machine's own voice: its lights, its coil,
# and the exact change it can never quite make when someone worth
# noticing walks past.
PICKUP_LINE = (
    "Are you exact change? Because every time you walk by, all my lights "
    "come on, my coil spins for nothing, and I can't make change for "
    "anyone else."
)

MAX_CHARS = 200


def main() -> None:
    line = PICKUP_LINE.strip()
    if not line:
        raise SystemExit("pickup line must not be empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"pickup line is {len(line)} chars, over the 200 limit")
    if "\n" in line:
        raise SystemExit("pickup line must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
