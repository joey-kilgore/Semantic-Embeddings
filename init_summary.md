# BCP & Bible Semantic Embedding Research

## Project Summary & Next Steps

---

## Project Vision

A computational theology project using semantic embeddings to analyze the relationship between the **Book of Common Prayer (BCP)** and the biblical corpus (ESV/KJV). The central research questions are:

1. **What percentage of the BCP is genuinely semantically derived from Scripture — and what does "derived" actually mean computationally?** (Interrogating the traditional "85% of the BCP is Scripture" claim)
2. **What passages in the BCP have the lowest semantic alignment to any biblical text — and what does that tell us theologically?**

This is framed as a _theological_ study that uses computational methods as tools, not as a machine learning paper that happens to touch theology.

---

## Core Research Questions

### Primary Question

The "85% of the BCP is Scripture" claim is a **threshold question disguised as a factual claim**. No one has formally defined what "derived from Scripture" means computationally. This project proposes to:

- Reverse-engineer what that threshold looks like in embedding space
- Calibrate it against known anchor cases (verbatim quotations at the high end; rubrics/administrative text at the low end)
- Produce a **precision-recall curve for scriptural derivation** — showing how the percentage changes as the similarity threshold moves
- Ask: _what does the 85% claim actually capture, and is it theologically meaningful?_

### Secondary Question

**Outlier detection**: What BCP passages fall below any reasonable threshold? These cluster into a typology:

|Tier|Similarity|Interpretation|
|---|---|---|
|High|~0.85–0.95|Direct quotation / verbatim paraphrase|
|Medium|~0.60–0.85|Theologically derived — synthesizing multiple biblical themes (e.g., a collect drawing simultaneously from Ps 139, Heb 4, 1 Jn)|
|Low|<0.60|Semantically distinct — Anglican tradition, Cranmerian theology, or post-biblical ecclesiastical doctrine operating independently|

The low-similarity tier is the most theologically interesting — not necessarily "unbiblical," but representing a _different mode_ of theological reasoning than direct scriptural derivation.

---

## Methodology

### Step 1: Corpus Preparation

- **Bible**: Start with KJV (freely available, public domain). Segment by verse (~31,000 segments).
- **BCP**: Segment by prayer/collect/section (~2,000–4,000 segments depending on edition). Prioritize the **1662 BCP** as the Anglican standard, then add 1928 (American), 1979 (TEC), and 2019 (ACNA) for edition comparison.
- **ESV**: Pending Crossway academic license (email sent). This is the preferred translation given its linguistic register matches the BCP's formal English.

### Step 2: Embedding Pipeline

Use `sentence-transformers` library. Core code is model-agnostic — model is a single swap:

```python
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-mpnet-base-v2')  # swap this line to change models
embeddings = model.encode(sentences, batch_size=32, show_progress_bar=True)
np.save('embeddings/bible_mpnet.npy', embeddings)
```

Save embeddings to named files per model so model comparison is built in from the start:

```
embeddings/
  bible_kjv_mpnet.npy
  bible_esv_mpnet.npy
  bcp_1662_mpnet.npy
  bcp_1979_mpnet.npy
  ...
```

### Step 3: Similarity Analysis

- Compute cosine similarity between all BCP segments and all Bible verses
- For each BCP segment: record its **maximum similarity score** (best biblical match), the **verse it matches**, and the **book/genre** of that verse
- Threshold sensitivity analysis: sweep threshold from 0.5–0.95 and plot what percentage of BCP segments have _at least one_ biblical match above threshold → this produces the calibration curve

### Step 4: Deeper Analysis (beyond raw similarity)

**Genre clustering**: Cluster the biblical corpus by genre first (Law, Prophecy, Wisdom, Psalms, Gospel, Epistle, Apocalyptic). Then ask which genre clusters BCP prayers land nearest → reveals the "theological grammar" of Anglican worship.

**Edition trajectory**: Embed 1662 → 1928 → 1979 → 2019. Compute direction vectors between editions. Is the liturgy moving _toward_ or _away_ from the Psalms? The Pauline epistles? This is directly relevant to the controversies around the 1979 revision.

**Concept anchoring**: Define theological concept vectors by averaging all verses about a given theme (atonement, covenant, resurrection, judgment). Ask where each BCP prayer falls relative to these anchors — produces a "theological coordinate system."

**Cross-testament bridging**: Find cases where an OT passage and an NT passage are _both_ highly similar to the same BCP text. These triplets are the BCP functioning as a semantic bridge between the testaments.

---

## Technical Decisions

### Model Selection

**Primary recommendation**: `all-mpnet-base-v2` or `e5-large-v2`

- Fits comfortably in 6GB VRAM (GTX 1060)
- Well-optimized for cosine similarity
- Good abstraction capacity for theological language

**Token length is critical**: Many BCP prayers exceed 512 tokens. Prefer models with longer context windows. `e5-large-v2` supports 512; newer models like `jina-embeddings-v2` support 8192. A model that reads the whole prayer beats a larger model that truncates halfway through.

**Avoid for this task**: Raw LLaMA/decoder models — they're not natively optimized for similarity comparison and add complexity without clear gain.

### Model Comparison Strategy

Run the same pipeline with 2–3 models and compare _results_ (similarity rankings, outlier sets, threshold curves) rather than raw vectors. Suggested comparison set:

1. `all-mpnet-base-v2` (baseline, fast)
2. `e5-large-v2` (stronger, longer context)
3. Optionally: domain-adapted model (see below)

### Domain-Adaptive Pre-Training

**Do this last, not first.** The sequence is:

1. Run baseline → get results → determine if they're interesting
2. If yes: fine-tune a base model on biblical/liturgical corpus (KJV + ESV + BCP editions + Church Fathers in public domain)
3. Compare domain-adapted results to baseline → the _difference_ is itself a finding

This is called **domain-adaptive pre-training** (DAPT). Your GTX 1060 can handle it for a corpus this size, but it takes 1–2 days. The `bible-nlp` organization on HuggingFace has training corpora already assembled.

---

## Suggested Implementation Order

|Phase|Task|Notes|
|---|---|---|
|1|Get KJV in clean plain text, segment by verse|Freely available from multiple sources|
|2|Get BCP 1662 in clean plain text, segment by prayer|May need some text cleaning work|
|3|Run baseline embeddings with `all-mpnet-base-v2`|Save to .npy files|
|4|Compute BCP→Bible similarity matrix (BCP×Bible, not full Bible×Bible)|~8M pairs, very manageable|
|5|Build threshold calibration curve|Core research finding #1|
|6|Identify and analyze outlier set|Core research finding #2|
|7|Swap in ESV once Crossway license arrives|Compare to KJV results|
|8|Run with `e5-large-v2`, compare|Model comparison finding|
|9|Add BCP edition comparison (1979, 2019)|Edition trajectory analysis|
|10|Domain-adaptive pre-training if warranted|Only if baseline results are compelling|

---

## Publication Strategy

The theological framing is a strategic advantage. Target audience: liturgical theologians and Anglican scholars who care about the BCP's scriptural grounding — not ML researchers.

### Primary Venues

**Zygon: Journal of Religion and Science** → zygonjournal.org

- Best established reputation (founded 1966)
- Diamond open access since 2024 — no author fees, no reader paywalls
- ~45% acceptance rate, ~2 month editorial decision
- Audience: scientists and theologians both; wants theological question driving the science
- Frame as: _"What does computational semantics reveal about the scriptural grounding of Anglican liturgy?"_

**Cursor: Zeitschrift für explorative Theologie** → cursor.pubpub.org

- Directly connected to the Heidelberg TheoLab / computational theology community
- More experimental tone; accepts working drafts ("Explorations") as well as peer-reviewed "Pubs"
- Best venue if you want to reach the computational theology specialist community
- Open access

**Open Theology (De Gruyter)** → degruyter.com/journal/key/opth/html

- Peer-reviewed, open access, broader scope
- Has published digital humanities / biblical studies work
- Good fallback; reaches theologians open to new methods

**Digital Biblical Studies (Brill)** → brill.com/display/serial/DBS

- Book series, not a journal — for a longer monograph treatment later
- Would be appropriate if the project expands to include multiple liturgical traditions

### Key Framing for Publication

The novel contribution is **not** "we built an embedding pipeline." It is:

- The first formal computational definition of what "derived from Scripture" means metrically
- A precision-recall curve for scriptural derivation (a concept that doesn't exist in liturgical scholarship)
- A map of how the BCP relates to Scripture at multiple levels of semantic proximity
- Identification of the theologically distinct passages that fall outside any reasonable threshold

### Potential Collaboration

A co-author with theological credentials would significantly strengthen submissions to theology journals. Consider whether a theologian at GWU, at Christ the King Anglican, or in the broader Anglican academic community might want to collaborate.

---

## Background: Why Semantic Embeddings?

Semantic embeddings represent words/sentences as vectors in high-dimensional space, where geometric proximity corresponds to semantic similarity. The key insight (from Mikolov et al. 2013) is that meaningful conceptual relationships appear as linear algebraic relationships in this space.

For this project, the relevant properties are:

- **Cosine similarity**: Measures the angle between two vectors — 1.0 = identical meaning, 0.0 = unrelated, -1.0 = opposite
- **Centroid**: The average of multiple vectors — represents the "semantic center" of a set of texts
- **Distributional semantics**: Words/phrases that appear in similar contexts get similar vectors — meaning is captured from usage patterns

The Peterson intuition that motivated this project (the centroid of all "good" words ≈ "God" in semantic space) is a specific instance of this centroid logic. Your project applies the same logic more rigorously to a falsifiable theological question.

---

## Key Resources

### Libraries

- `sentence-transformers` (HuggingFace) — core embedding library
- `numpy` — vector math, storing embeddings
- `faiss` — efficient similarity search at scale
- `sklearn` — cosine similarity, clustering
- `matplotlib` / `seaborn` — visualization

### Foundational Papers

- Mikolov et al. 2013 — word2vec
- Pennington et al. 2014 — GloVe
- Reimers & Gurevych 2019 — Sentence-BERT (the paper behind sentence-transformers)
- Caliskan et al. 2017 — moral/social geometry in embedding space (Science)

### Background Reading

- Jay Alammar's "The Illustrated Word2Vec" — best visual introduction
- Jay Alammar's "The Illustrated BERT"
- HuggingFace NLP Course (huggingface.co/learn/nlp-course) — Chapters 1–2

### Computational Theology Context

- _Compendium of Computational Theology_ Vol. 1 (Nunn & van Oorschot, Heidelberg 2024) — open access at heiBOOKS
- TheoLab at Heidelberg University (theologie.uni-heidelberg.de/theolab)
- bible-nlp organization on HuggingFace — training corpora and models

---

_Summary compiled from research conversation, May 2026_