"""Copier entrypoint: prints entry.txt and copies it to the output dir."""

import os
from pathlib import Path

ASSET = Path(__file__).resolve().with_name("entry.txt")


def load_entry():
    raw = ASSET.read_bytes()
    return raw.decode("utf-8").strip()


def main():
    text = load_entry()
    print(text)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
