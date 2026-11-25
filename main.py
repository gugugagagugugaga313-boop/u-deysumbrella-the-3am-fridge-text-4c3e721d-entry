"""The 3AM Fridge Text — one line a smart fridge texts its owner at 3am.

Deterministic: no input, no randomness, no network, no clock.
Writes the exact line to /output/entry.txt.
The line is a single text message, 115 characters, one line, no trailing
newline — the sealed gate counts characters, so the output is exactly the line.
"""

import os

LINE = "3am. You open me like I'm a slot machine. There's no jackpot in here \u2014 just the same yogurt and your bad decisions."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
