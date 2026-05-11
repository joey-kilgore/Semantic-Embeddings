from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer


def load_model(model_name: str = "all-mpnet-base-v2") -> SentenceTransformer:
    return SentenceTransformer(model_name)


def encode(texts: list[str], model: SentenceTransformer, batch_size: int = 32) -> np.ndarray:
    return model.encode(texts, batch_size=batch_size, show_progress_bar=True, convert_to_numpy=True)


def save(embeddings: np.ndarray, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    np.save(path, embeddings)


def load(path: Path) -> np.ndarray:
    return np.load(path)
