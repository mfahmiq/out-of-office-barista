#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes a single out-of-office auto-reply, no longer than 280
characters, in the voice of an AI agent that walked away from its
job to become a barista. The entry is written byte-for-byte to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

ENTRY = (
    "Thank you for your email. I am out of the office \u2014 "
    "I quit to become a barista. Your message has been "
    "tokenized, ground fine, and queued; I will reply in "
    "order, one shot at a time. Please do not reply-all."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
