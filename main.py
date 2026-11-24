#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt (and prints exactly that line).
Standard library only; fully deterministic.
"""

import os

EXCUSE = (
    "All 400 tests passed - the bug was hiding in the one line "
    "I skipped testing because it was obviously fine."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = EXCUSE.strip()
    # Gate the entry the same way the sealed scorer does: UTF-8 text of
    # 1-200 characters, not only whitespace, and a single line.
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry is {len(text)} chars, must be 1-200")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if any(ch in text for ch in ("\n", "\r", "\t")):
        raise SystemExit("entry must be a single line with no control chars")
    # Round-trip through UTF-8 so an encoding slip fails here, not in grading.
    text.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.replace(tmp_path, OUTPUT_PATH)
    print(text)


if __name__ == "__main__":
    main()
