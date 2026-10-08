---
title: 'Exercise: Simulate three station feeds'
slug: exercise-seeded-random-samples
order: 8
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Use a seeded local generator for integer, uniform, and normal distributions.
seo_title: 'Exercise: Simulate three station feeds | NumPy for beginners'
seo_description: Use a seeded local generator for integer, uniform, and normal distributions.
seo_keywords:
  - NumPy
  - Python arrays
  - exercise seeded random samples
---

The station needs three synchronized sample feeds. Create **one** local generator per call; its draws form a sequence, so drawing integers, then uniform fractions, then normal noise in that order matters. `uniform(0, 1)` samples between 0 and 1; `normal(0, 1)` samples from a distribution centered on 0 with standard deviation 1.

The starter's `simulate_feeds` returns `None`. Edit `main.py`, press **Run** to see the three arrays, then **Submit** to check replay with another seed and length.

## Your Tasks

1. Make `simulate_feeds(seed, count)` create one `np.random.default_rng(seed)`, draw `integers(0, 10, size=count)`, then `uniform(0, 1, size=count)`, then `normal(0, 1, size=count)`, and return the three arrays in that order.
