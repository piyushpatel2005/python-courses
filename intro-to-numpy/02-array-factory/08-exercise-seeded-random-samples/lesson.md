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

Build three test feeds: event counts, uniform fractions, and normally distributed noise. The starter creates one seeded generator per function call and returns a tuple with a place for each feed. Replace one `None` at a time; the print call works even while some feeds are unfinished.

Use the supplied `rng` for every draw. Keep the order shown: integers, then uniform fractions, then normal noise. Creating a new generator for each line would restart the sequence and change the results.

## Your Tasks

1. Set `counts` to `rng.integers(0, 10, size=count)`.
2. Set `fractions` to `rng.uniform(0, 1, size=count)`.
3. Set `noise` to `rng.normal(0, 1, size=count)`.

Edit `main.py`, press **Run** to inspect the three feeds, then **Submit** to check another seed and length. Each slot is checked separately, so you can check your progress after the first draw.
