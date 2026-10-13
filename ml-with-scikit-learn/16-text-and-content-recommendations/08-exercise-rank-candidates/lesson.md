---
title: "Exercise: rank eligible recommendations"
slug: "exercise-rank-candidates"
order: 8
lesson_type: "coding"
runtime: "pyodide"
pyodide_packages:
  - "numpy"
  - "scikit-learn"
  - "pandas"
language: "python"
summary: "Exclude the query item and seen items and sort scores with stable ID tie breaking."
seo_title: "Exercise: rank eligible recommendations | Scikit-learn practice"
seo_description: "Exclude the query item and seen items and sort scores with stable ID tie breaking. Work with small, inspectable examples."
seo_keywords:
  - "scikit-learn"
  - "rank candidates"
  - "Python practice"
---

Similarity scores are not yet a recommendation list. Remove the query item and every previously seen item before selecting results. Otherwise the highest-ranked result may be a product the user already opened.

Keep IDs aligned with their scores. Sort candidate pairs by `(-score, item_id)`: the negative sign makes larger scores appear first, and the second key resolves exact ties by ascending stable ID. Never rely on the incoming catalog order to settle ties. Return IDs only, with no duplicates and at most `k` results. If fewer eligible products remain, return a shorter list.

The supplied arrays contain exact ties so the policy is visible. This function accepts finite scores and unique item IDs as its input contract. It is a ranking operation, not a fitted estimator. Filtering after slicing the top scores would lose eligible replacements, so filter first.

The exercise uses a separate supplied fixture. Write the helper body rather than copying the preceding output; the checks call it with other inputs as well.

These are original synthetic fixtures. The fixed teaching snapshot is 2025-01-15; only declared training partitions may fit state.

### Fixture fields

| Field | Type and units | Role |
|---|---|---|
| `ids / query_id / seen` | unique strings / string / set of strings | candidate alignment / self exclusion / history exclusions |
| `scores` | finite float list aligned to ids, no unit | supplied ranking scores |
| `k` | positive integer, items | requested cutoff |

## Your Tasks

1. Implement `rank_items(ids, scores, seen, query_id, k)` to exclude seen/self IDs, sort by descending score then ascending ID, and return at most `k` distinct IDs.

Edit `main.py`, press Run to inspect the supplied checkpoint, then Submit to check the helper. The probe is supplied; you do not need to add printing.
