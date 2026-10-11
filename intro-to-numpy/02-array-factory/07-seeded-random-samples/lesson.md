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

Random samples let you test code before you have measurements. `np.random.default_rng(seed)` creates a local generator. A seed is a starting value: fresh generators with the same seed repeat the same draws when you make the same calls in the same order. Calling an existing generator again advances its sequence instead of restarting it. These examples are for repeatable testing, not security; exact sequences are not promised across all NumPy versions.

`integers(low, high, size=...)` includes `low` and excludes `high`. The starter draws four scores twice from fresh generators with seed `21`. `np.array_equal(first, again)` prints whether the two arrays match.

The separate `effects` generator demonstrates two other distributions:

- `uniform(0, 1, size=3)` draws three fractions from 0 to 1, with equal likelihood across that interval and normally excluding 1. The three results need not be evenly spaced. Floating-point rounding can sometimes include the upper bound.
- `normal(0, 1, size=3)` draws three values from a bell-shaped distribution centered on 0. The standard deviation, `1`, controls its spread; it is not an upper bound. A small sample need not average exactly 0.

The `.round(2)` calls only shorten the printed decimals. Leave these sound-effect draws unchanged.

## Your Task

1. Set `upper_bound` to `10` so both integer draws use the new exclusive limit.

Edit `main.py`, press **Run** to compare the scores, then **Submit**. Both arrays should still match.
