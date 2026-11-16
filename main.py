#!/usr/bin/env python3
"""Sky Jelly — place the entry image where the judge expects it.

The image itself is the entry. This script only carries it, byte for
byte, from next to this file to /output/entry.png, so the result is
fully deterministic: the same input always yields the same output.
"""

import hashlib
import os
import shutil
import sys


def sha256_of(path):
    """Return the hex sha256 of the file at path."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = "/output"
    target = os.path.join(out_dir, "entry.png")

    if not os.path.isfile(source):
        print(f"missing input image: {source}", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, target)

    checksum = sha256_of(target)
    print(f"wrote {target} (sha256 {checksum})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
