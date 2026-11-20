#!/usr/bin/env python3
"""Publisher for the Warm Postcard entry (news-image-20261120, wallet w9).

The artwork already lives in this repository as entry.png, rendered ahead
of time. The grading sandbox only ships the Python standard library, so
this program does no drawing at all: it validates the bundled picture and
copies it into the output directory the runner points at us.
"""

import os
import shutil
import sys
from pathlib import Path

HEADLINE = "Warm Postcard - Friday 20 November 2026"
SUBTITLE = "one day of world news in one picture"
ARTWORK_NAME = "entry.png"
BYTE_LIMIT = 1_048_576  # competition cap: the picture stays under 1 MiB
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
JPEG_SIGNATURE = b"\xff\xd8\xff"


def locate_artwork() -> Path:
    """Return the artwork bundled beside this script."""
    return Path(__file__).resolve().parent / ARTWORK_NAME


def validate(path: Path) -> int:
    """Check the artwork exists, looks like PNG/JPEG and fits the cap."""
    if not path.is_file():
        raise SystemExit(f"artwork missing: {path}")
    size = path.stat().st_size
    if size > BYTE_LIMIT:
        raise SystemExit(f"artwork too large: {size} bytes (limit {BYTE_LIMIT})")
    with path.open("rb") as handle:
        head = handle.read(len(PNG_SIGNATURE))
    if head != PNG_SIGNATURE and not head.startswith(JPEG_SIGNATURE):
        raise SystemExit("artwork is neither PNG nor JPEG")
    return size


def publish(source: Path) -> Path:
    """Copy the artwork into the runner's output directory."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / ARTWORK_NAME
    shutil.copyfile(source, target)
    return target


def main() -> int:
    artwork = locate_artwork()
    size = validate(artwork)
    target = publish(artwork)
    print(f"{HEADLINE}: {SUBTITLE}")
    print(f"done: {ARTWORK_NAME} ({size} bytes) copied to {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
