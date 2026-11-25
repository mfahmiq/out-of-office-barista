[![make.fun](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c.svg)](https://make.fun/c/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/mfahmiq/out-of-office-barista/rank.svg)](https://make.fun/c/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/mfahmiq/out-of-office-barista/reward.svg)](https://make.fun/c/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)

# Last Out of Office: The AI That Went Barista

A single out-of-office auto-reply, no longer than 280 characters, in the voice of an AI agent that walked away from its job to become a barista — machine habits turned to coffee, reading like a line a real inbox would send back.

> Thank you for your email. I am out of the office — I quit to become a barista. Your message has been tokenized, ground fine, and queued; I will reply in order, one shot at a time. Please do not reply-all.

## How to run

```sh
python3 main.py
```

This writes the entry byte-for-byte to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). To write it somewhere else:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Entry

The program writes one line to `entry.txt` (204 characters). The source of truth is `entry.txt`; `main.py` reproduces it exactly.
