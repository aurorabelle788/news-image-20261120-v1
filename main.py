#!/usr/bin/env python3
"""news-image-20261120 entry.

One image summing up Friday 20 November 2026 world news: a newspaper
front page (1024x1024) with the 15 verified stories, each with its own
thumbnail and its source printed beneath it.

The image is the entry.png beside this file. This program copies it to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).

Standard library only: no third-party packages, no network, no clock,
no randomness. The output bytes are exactly the repository's entry.png.
"""

import os
import shutil

IMAGE_NAME = "entry.png"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, IMAGE_NAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, IMAGE_NAME)
    shutil.copyfile(source, target)
    # Confirm the copy landed whole before reporting success.
    if os.path.getsize(target) != os.path.getsize(source):
        raise SystemExit("entry.png copy is incomplete")
    print("wrote " + target)


if __name__ == "__main__":
    main()
