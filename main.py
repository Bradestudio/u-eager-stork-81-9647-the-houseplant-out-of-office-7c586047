"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, as if a houseplant sent it, to
/output/entry.txt. The line is the whole entry: at most 120 characters.
"""

import os
from pathlib import Path

ENTRY = (
    "Out of office. I am the fern you ignored since March. "
    "The cactus is covering my inbox. It has never once needed you."
)

MAX_CHARS = 120


def main() -> None:
    # No trailing newline: the gate counts every character, 1-120.
    text = ENTRY.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars, must be 1-120"
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
