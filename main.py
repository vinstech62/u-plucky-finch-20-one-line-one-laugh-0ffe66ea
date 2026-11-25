#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single funny line of text to /output/entry.txt.

The line is fixed and deterministic: the same line is written on every
run, so the entry is identical across repeated runs and re-grades.

The joke: a smartwatch nags its wearer to stand up. The wearer obeys —
then sits straight back down out of spite. Setup, compliance, defiance:
a complete little arc in one line, no picture or setup needed.
"""

from pathlib import Path

LINE = "My smartwatch says I need to stand up, so I stood up and sat back down out of spite."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE + "\n", encoding="utf-8")
    OUTPUT.chmod(0o644)


if __name__ == "__main__":
    main()
