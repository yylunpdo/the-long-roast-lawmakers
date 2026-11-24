#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence (1-320 characters) to /output/entry.txt.
Pure Python standard library only.
"""

import os

ENTRY = (
    "They passed a 212-page law telling AI exactly how to think, then spent "
    "three hours on hold with IT because nobody in the room could turn the "
    "draft into a PDF, and the hearing on the future of the internet was "
    "postponed until someone finds the button."
)


def main():
    # Gate (RULES.txt): /output/entry.txt, UTF-8, 1-320 chars, one sentence.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    assert 1 <= len(text) <= 320, f"entry length {len(text)} out of gate 1-320"
    assert text.strip(), "entry must not be only whitespace"
    assert text.count("\n") == 0, "entry must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
