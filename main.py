"""Sky Jelly — make.fun ai-excited-01 entry (Python 3.13, standard library only).

The entry image is the file entry.png beside this script: a colossal
aurora-lit jellyfish the size of a skyscraper drifting over a tiny
lantern-lit fishing harbor at dusk, one lone fisherman looking up in awe.
This program copies it, byte for byte, to /output/entry.png, so the
judge sees exactly the bytes in the repository.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUTPUT_DIR / "entry.png")
