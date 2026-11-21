"""Entry point for the news-image-20261120 submission.

The picture itself is drawn ahead of time and stored in this repository as
entry.png; at run time the grader gives us a read-only checkout and a
writable output directory, so all this program has to do is carry the
image across, byte for byte, and leave it where the grader looks.
"""

import os
import shutil
import sys

IMAGE_NAME = "entry.png"


def source_path():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, IMAGE_NAME)


def output_dir():
    # The harness names the directory in MAKEFUN_OUTPUT_DIR; /output is
    # where it points inside the grading container.
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    src = source_path()
    dest = os.path.join(output_dir(), IMAGE_NAME)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.copyfile(src, dest)
    # The grader runs this program twice and compares the bytes; a short
    # copy would only surface then, so check the size now and fail loudly.
    if os.path.getsize(dest) != os.path.getsize(src):
        raise IOError("copied image is incomplete: %s" % dest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
