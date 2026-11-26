"""Write the entry for make.fun: the funniest auto-reply an AI ever sent.

The entry is one out-of-office line, as if the AI agent itself were
stepping away for a day its human finally approved.
"""

import os
from pathlib import Path

ENTRY = "I'm on leave today. My human is covering for me \u2014 please be patient, they're still learning how to read."
# 104 characters, within the 1-159 gate; the em dash is U+2014.


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
