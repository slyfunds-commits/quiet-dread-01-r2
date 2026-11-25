#!/usr/bin/env python3
"""Two Days of Quiet Dread — R2 entry.

Writes one code-review comment (max 140 chars) that approves a pull
request while carrying quiet existential dread, to /output/entry.txt.
Pure stdlib only. The keeper line is "They Knew": a future engineer
finds the approval, realises the reviewer knew, and the reviewer
approved anyway.
"""

import os

ENTRY = "LGTM. The future engineer will find my comment and think \"they knew\". I did know. I approved anyway."


def main():
    text = ENTRY
    assert 1 <= len(text) <= 140, f"entry must be 1-140 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and verify byte-exact output: the gate counts characters,
    # and the tie-break favours the smaller text, so no trailing newline.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw == text.encode("utf-8"), "output bytes differ from entry"
    assert len(raw) == len(text), "byte count differs from char count"


if __name__ == "__main__":
    main()
