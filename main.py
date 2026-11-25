#!/usr/bin/env python3
"""One-line slogan for a Solana wallet agent.

Writes a single original slogan to entry.txt.
Stdlib only, no network, no file reads outside the repo.
"""
import os

SLOGAN = "Your Solana wallet agent handles the paying, the swapping, the saving \u2014 you handle the living."

assert "\n" not in SLOGAN, "slogan must be a single line"
assert 1 <= len(SLOGAN) <= 135, "slogan must be 1-135 chars"
assert len(SLOGAN.split()) <= 20, "slogan must be at most 20 words"
assert SLOGAN.strip(), "slogan must not be only whitespace"

out_dir = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(SLOGAN)
