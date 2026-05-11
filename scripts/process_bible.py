"""Process raw KJV CSV into segmented JSON for embedding.

Usage:
    python scripts/process_bible.py

Reads:  data/raw/kjv.csv
Writes: data/processed/bible_kjv.json
"""

from pathlib import Path
import sys

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "src"))

from sacred_semantics.corpus.bible import load_kjv, segment_by_verse, save_segments

RAW = ROOT / "data" / "raw" / "kjv.csv"
OUT = ROOT / "data" / "processed" / "bible_kjv.json"


def main() -> None:
    if not RAW.exists():
        print(f"Error: {RAW} not found. Download KJV CSV from scrollmapper/bible_databases.")
        sys.exit(1)

    print(f"Loading {RAW} ...")
    raw = load_kjv(RAW)

    print("Segmenting by verse ...")
    segments = segment_by_verse(raw)

    ot = sum(1 for s in segments if s["testament"] == "OT")
    nt = sum(1 for s in segments if s["testament"] == "NT")
    print(f"  {len(segments)} verses  |  OT: {ot}  NT: {nt}")

    print(f"Saving to {OUT} ...")
    save_segments(segments, OUT)
    print("Done.")


if __name__ == "__main__":
    main()
