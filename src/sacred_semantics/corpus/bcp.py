from pathlib import Path


def load_section(path: Path) -> str:
    """Load raw text for a single BCP 2019 section from a plain-text file."""
    return path.read_text(encoding="utf-8")


def segment_by_prayer(text: str, section: str) -> list[dict]:
    """Split a BCP section into individual prayer/collect segments.

    Each record has keys: section, title, text.
    """
    raise NotImplementedError
