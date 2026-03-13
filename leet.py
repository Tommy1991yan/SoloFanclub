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

HR = "─" * 40


def to_leet(text: str) -> str:
    return "".join(LEET_MAP.get(c.lower(), c) for c in text)


def print_output(text: str):
    print(f"\n{HR}\n")
    print(text)
    print(SOLO_CAN)
    print(f"\n{HR}\n")


def main():
    if len(sys.argv) > 1:
        print_output(to_leet(" ".join(sys.argv[1:])))
    else:
        print("Enter text (Ctrl+D to quit):", file=sys.stderr)
        try:
            for line in sys.stdin:
                print_output(to_leet(line.rstrip("\n")))
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
