---
title: Replay seeded samples
slug: seeded-random-samples
order: 7
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Draw integer, uniform, and normal samples with local seeded generators.
seo_title: Replay seeded samples | NumPy for beginners
seo_description: Draw integer, uniform, and normal samples with local seeded generators.
seo_keywords:
  - NumPy
  - Python arrays
  - seeded random samples
---

The arcade replays a test round with a fresh `np.random.default_rng(seed)` generator. Its `integers(low, high, size=...)` call excludes `high`. A seed replays the same draw sequence for testing, not for cryptographic security; a local generator avoids changing global random state. The second generator models sound effects: `uniform(0, 1, size=...)` draws fractions and `normal(0, 1, size=...)` draws noise centered on 0 with standard deviation 1. Each call advances that generator's sequence.

Edit `main.py`, press **Run** to compare the four integer draws before and after changing the bound; both seeded integer draws should still match. The sound-effect draws stay the same. Then **Submit**.

## Your Task

1. Change both integer calls’ exclusive upper bounds from 6 to 10 so replay still matches.
