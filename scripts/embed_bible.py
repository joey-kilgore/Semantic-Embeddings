"""Generate embeddings for the processed KJV corpus and save to .npy.

Usage:
    python scripts/embed_bible.py
    python scripts/embed_bible.py --model e5-large-v2

Reads:  data/processed/bible_kjv.json
Writes: embeddings/bible_kjv_<model-slug>.npy
"""

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "src"))

from sacred_semantics.corpus.bible import load_segments
from sacred_semantics.pipeline.embed import encode, load_model, save

PROCESSED = ROOT / "data" / "processed" / "bible_kjv.json"
EMBEDDINGS = ROOT / "embeddings"


def model_slug(model_name: str) -> str:
    return model_name.replace("/", "_").replace("-", "_")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="all-mpnet-base-v2")
    parser.add_argument("--batch-size", type=int, default=32)
    args = parser.parse_args()

    if not PROCESSED.exists():
        print(f"Error: {PROCESSED} not found. Run scripts/process_bible.py first.")
        sys.exit(1)

    out_path = EMBEDDINGS / f"bible_kjv_{model_slug(args.model)}.npy"
    if out_path.exists():
        print(f"Embeddings already exist at {out_path}. Delete to re-run.")
        sys.exit(0)

    print(f"Loading segments from {PROCESSED} ...")
    segments = load_segments(PROCESSED)
    texts = [s["text"] for s in segments]
    print(f"  {len(texts)} verses")

    print(f"Loading model {args.model!r} ...")
    model = load_model(args.model)

    print("Encoding ...")
    embeddings = encode(texts, model, batch_size=args.batch_size)
    print(f"  Embedding shape: {embeddings.shape}")

    print(f"Saving to {out_path} ...")
    save(embeddings, out_path)
    print("Done.")


if __name__ == "__main__":
    main()
