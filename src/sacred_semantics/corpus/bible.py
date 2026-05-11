import csv
import json
from pathlib import Path

from .books import BOOK_INDEX


def load_kjv(path: Path) -> list[dict]:
    """Load KJV verses from a CSV with columns: Book, Chapter, Verse, Text."""
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def segment_by_verse(raw: list[dict]) -> list[dict]:
    """Normalize raw CSV records into verse segments.

    Each output record has keys: book, chapter, verse, ref, text, testament, genre.
    Record order is stable — index N here corresponds to row N in the embedding array.
    """
    segments = []
    for row in raw:
        book_name = row["Book"]
        book = BOOK_INDEX[book_name]
        chapter, verse = int(row["Chapter"]), int(row["Verse"])
        segments.append({
            "book": book_name,
            "chapter": chapter,
            "verse": verse,
            "ref": f"{book_name} {chapter}:{verse}",
            "text": row["Text"],
            "testament": book.testament,
            "genre": book.genre,
        })
    return segments


def save_segments(segments: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(segments, f, ensure_ascii=False, indent=2)


def load_segments(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        return json.load(f)
