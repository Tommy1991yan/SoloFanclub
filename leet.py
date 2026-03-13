#!/usr/bin/env python3
"""English to 1337speak translator."""

import sys

LEET_MAP = {
    "a": "4",
    "e": "3",
    "i": "1",
    "l": "1",
    "o": "0",
    "s": "5",
    "t": "7",
}


SOLO_CAN = r"""
     ________
    |        |
    | S O L O|
    |  ~~~~  |
    | /    \ |
    ||      ||
    ||      ||
    | \    / |
    |________|
"""


def to_leet(text: str) -> str:
    return "".join(LEET_MAP.get(c.lower(), c) for c in text)


def main():
    if len(sys.argv) > 1:
        print(to_leet(" ".join(sys.argv[1:])))
        print(SOLO_CAN)
    else:
        print("Enter text (Ctrl+D to quit):", file=sys.stderr)
        try:
            for line in sys.stdin:
                print(to_leet(line), end="")
                print(SOLO_CAN)
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
