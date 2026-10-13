---
title: "Exercise: reward relevant items near the top"
slug: "exercise-ndcg"
order: 6
lesson_type: "coding"
runtime: "pyodide"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "pandas"
language: "python"
summary: "Compute binary relevance DCG and normalized DCG with an explicit zero-IDCG policy."
seo_title: "Exercise: reward relevant items near the top | Scikit-learn practice"
seo_description: "Compute binary relevance DCG and normalized DCG with an explicit zero-IDCG policy. Work with small, inspectable examples."
seo_keywords:
  - "scikit-learn"
  - "ndcg"
  - "Python practice"
---

Precision@k cannot distinguish a hit in first position from the same hit in third. Discounted cumulative gain rewards earlier relevant results. Binary relevance assigns gain one to a relevant item and zero otherwise. Divide DCG by the best possible DCG for that user's relevance set to obtain NDCG.

The ranking is already in deterministic order; this helper does not sort scores. Missing positions contribute zero, and duplicate IDs receive gain only on their first occurrence. The ideal list has `min(k, len(relevant))` hits first. If there are no relevant items, return zero for this helper; the evaluation caller can omit that user when computing macro metrics according to its eligibility policy.

`np.log2` computes the base-two logarithm used in the discount. The first position has denominator log2(2)=1, so its gain is unchanged. This is binary NDCG; graded relevance would need a separately declared gain definition. Ranking scores are not relevance grades.

For binary gains $g_i$ at rank $i$,

$$
DCG@k=\sum_{i=1}^{k}\frac{g_i}{\log_2(i+1)}.
$$

Here $k$ is the cutoff, $g_i$ is one for a first occurrence of a relevant ID and zero otherwise, and missing ranks have zero gain. $IDCG@k$ is the same sum for the ideal ordering. For positive ideal gain,

$$
NDCG@k=\frac{DCG@k}{IDCG@k}.
$$

A sole relevant item at rank two gives $DCG=1/\log_2(3)\approx0.6309$. Its ideal position is first, with $IDCG=1$, so NDCG is 0.6309. These scores are unitless.

The exercise uses a separate supplied fixture. Write the helper body rather than copying the preceding output; the checks call it with other inputs as well.

These are original synthetic fixtures. The fixed teaching snapshot is 2025-01-15; only declared training partitions may fit state.

### Fixture fields

| Field | Type and units | Role |
|---|---|---|
| `ranked` | ordered list of string item IDs | recommended rank positions |
| `relevant` | set of string item IDs | binary held-out relevance proxy |
| `k` | positive integer, items | rank cutoff |

## Your Tasks

1. Implement `binary_ndcg(ranked, relevant, k)` with first-occurrence binary gains, logarithmic rank discounts, ideal normalization, and zero for empty relevance.

Edit `main.py`, press Run to inspect the supplied checkpoint, then Submit to check the helper. The probe is supplied; you do not need to add printing.
