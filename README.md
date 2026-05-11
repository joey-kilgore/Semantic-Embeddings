# Sacred Semantics

Semantic embedding analysis of theological and liturgical texts, with a focus on the relationship between the Book of Common Prayer (2019 ACNA) and the biblical corpus (KJV/ESV).

## Research Questions

1. What percentage of the BCP is genuinely semantically derived from Scripture — and what does "derived" mean computationally? (Interrogating the traditional "85% of the BCP is Scripture" claim)
2. Which BCP passages have the lowest semantic alignment to any biblical text, and what does that reveal theologically?

## Installation

```bash
pip install -e ".[dev]"
```

For GPU-accelerated similarity search, install the optional `search` group via conda:

```bash
conda install -c pytorch faiss-gpu
```

## Data

Source texts are not included in the repository and must be provided separately:

- **KJV Bible** — source from [scrollmapper/bible_databases](https://github.com/scrollmapper/bible_databases), place the CSV in `data/raw/` (see `notebooks/01_corpus_prep.ipynb`)
- **BCP 2019** — sections are added incrementally to `data/raw/bcp/` as they are sourced

Processed (segmented) JSON files live in `data/processed/` and are versioned. Embeddings (`.npy`) are gitignored due to size.

## Progress

- [x] Project scaffolding — package structure, `pyproject.toml`, directory layout
- [x] KJV corpus — acquired, segmented by verse with OT/NT labels
- [x] Save processed KJV segments to `data/processed/bible_kjv.json`
- [ ] Run baseline embeddings on KJV (`all-mpnet-base-v2`) → `embeddings/bible_kjv_mpnet.npy`
- [ ] BCP 2019 — source sections and implement segmentation
- [ ] Run baseline embeddings on BCP 2019 → `embeddings/bcp_2019_mpnet.npy`
- [ ] Compute BCP→Bible similarity matrix (~8M pairs)
- [ ] Threshold calibration curve (core finding #1)
- [ ] Outlier analysis — identify low-similarity BCP passages (core finding #2)
- [ ] Swap in ESV once Crossway license arrives
- [ ] Run with `e5-large-v2`, compare results
- [ ] BCP edition comparison (1662, 1979 trajectory analysis)
- [ ] Domain-adaptive pre-training (only if baseline results are compelling)

## Structure

```text
src/sacred_semantics/
  corpus/      # text ingestion and segmentation
  pipeline/    # embedding generation and storage
  analysis/    # similarity, calibration curves, clustering
data/
  raw/         # source texts (gitignored — provide your own)
  processed/   # segmented JSON records (versioned)
embeddings/    # .npy files per model/corpus (gitignored)
notebooks/     # exploratory analysis and results
```
