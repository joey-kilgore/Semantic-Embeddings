import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def max_similarity(bcp_embeddings: np.ndarray, bible_embeddings: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """For each BCP segment return its maximum cosine similarity and the index of the best-matching verse.

    Returns (scores, indices) each of shape (n_bcp,).
    """
    raise NotImplementedError


def threshold_curve(
    max_scores: np.ndarray,
    thresholds: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """Sweep similarity thresholds and return (thresholds, fraction_of_bcp_above_threshold).

    Core output for the scriptural-derivation calibration curve.
    """
    if thresholds is None:
        thresholds = np.linspace(0.5, 0.95, 91)
    fractions = np.array([(max_scores >= t).mean() for t in thresholds])
    return thresholds, fractions
