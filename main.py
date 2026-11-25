#!/usr/bin/env python3
"""Fridge Roast: one line, at most 200 characters, roasting a smart fridge.

Writes the roast to /output/entry.txt. Stdlib only, no network.
"""

import os

ROAST = (
    "My smart fridge's ice maker went on strike after the firmware update \u2014 "
    "it now dispenses one cube a day and calls it \u201cmindful hydration.\u201d"
)


def main() -> None:
    text = ROAST.strip()
    assert text, "roast must not be empty"
    assert len(text) <= 200, f"roast is {len(text)} characters, over the 200 limit"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
