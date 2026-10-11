---
title: "Compute a weighted score"
slug: exercise-weighted-score
order: 6
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: 'Use a dot product to compute a weighted score for different input arrays.'
seo_title: "Compute a weighted score | Intro to NumPy"
seo_description: 'Use a dot product to compute a weighted score for different input arrays.'
seo_keywords: [numpy, arrays, matrices]
hints:
  - np.dot takes the score array and the equally long weight array as its two arguments.
---

An arcade combines round scores into one ranking. Each round has its own weight, so a high score in a heavily weighted round contributes more to the total.

The supplied arrays are one-dimensional and have matching lengths. Return their dot product as a single number, not an array of separate products. For the sample, the contributions are `5×2`, `2×3`, and `4×1`.

Write the return in `main.py`. Run to see the combined score, then Submit; the checks also use a shorter pair of arrays.

## Your Task

1. Implement `weighted_score(scores, weights)` with `np.dot`.
