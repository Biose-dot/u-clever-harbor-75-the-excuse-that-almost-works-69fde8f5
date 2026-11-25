"""Copier entrypoint: copies the committed entry.txt asset to the output dir."""

import os
import shutil

ASSET = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def fallback_copy(src, dst):
    with open(src, "rb") as f:
        data = f.read()
    with open(dst, "wb") as f:
        f.write(data)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    try:
        shutil.copyfile(ASSET, dst)
    except Exception:
        fallback_copy(ASSET, dst)


if __name__ == "__main__":
    main()
