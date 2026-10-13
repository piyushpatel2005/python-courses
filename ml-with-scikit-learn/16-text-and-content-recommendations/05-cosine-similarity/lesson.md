---
title: "Compare item vectors by cosine"
slug: "cosine-similarity"
order: 5
lesson_type: "coding"
runtime: "pyodide"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "pandas"
language: "python"
summary: "Compute cosine_similarity and handle zero-vector similarity explicitly."
seo_title: "Compare item vectors by cosine | Scikit-learn practice"
seo_description: "Compute cosine_similarity and handle zero-vector similarity explicitly. Work with small, inspectable examples."
seo_keywords:
  - "scikit-learn"
  - "cosine similarity"
  - "Python practice"
---

Cosine similarity compares vector directions rather than raw magnitudes. Two proportional nonzero vectors have similarity one even if one is longer. Orthogonal vectors have similarity zero. For nonnegative TF-IDF features, scores lie between zero and one; arbitrary signed vectors can also have negative similarity.

`cosine_similarity(queries, items)` returns a dense matrix with one row per query and one column per item. This is small here. For a large catalog, score a small query batch rather than allocating all item pairs. Sparse input is accepted; the default result is dense.

The mathematical fraction is undefined for a zero vector. Scikit-learn handles a zero input row by returning zero similarities, including against itself. Treat that as a no-information case rather than strong dissimilarity. A later lesson chooses a fallback instead of relying on arbitrary zero-score ties.

For nonzero vectors $u$ and $v$,

$$
\cos(u,v)=\frac{u\cdot v}{\|u\|_2\|v\|_2}.
$$

The dot product $u\cdot v$ sums products of matching coordinates. Each L2 norm is the square root of the sum of squared coordinates. The ratio is unitless. For $u=[2,0]$ and $v=[1,1]$, the dot product is 2 and the norms are $2$ and $\sqrt2$, giving $1/\sqrt2\approx0.7071$. The library returns this value and separately defines zero-row similarities as zero.

![Query [2,0]; item [1,1]; Dot = 2; norms = 2 and sqrt(2); Cosine = 0.7071; zero query = 0](cosine-similarity-data-flow.svg)

The starter runs a comparison baseline. Replace the raw dot-product expression with cosine similarity.

These are original synthetic fixtures. The fixed teaching snapshot is 2025-01-15; only declared training partitions may fit state.

### Fixture fields

| Field | Type and units | Role |
|---|---|---|
| `items / queries` | sparse float matrices with matching feature columns | nonnegative illustrative feature weights; rows may be zero |

## Your Tasks

1. Implement `compare_vectors(queries, items)` using `cosine_similarity` and preserve its query-by-item shape and zero-row behavior.

Edit `main.py`, press Run to inspect the supplied checkpoint, then Submit to check the helper. The probe is supplied; you do not need to add printing.
