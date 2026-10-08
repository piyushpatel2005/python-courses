---
title: "Summarize both directions"
slug: exercise-grid-totals
order: 4
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Summarize both directions with NumPy arrays."
seo_title: "Summarize both directions | Intro to NumPy"
seo_description: "Practice summarize both directions in a runnable NumPy lesson."
seo_keywords: [numpy, arrays, statistics]
hints:
  - Read the shape of the input and the requested result before choosing an axis.
---

An arcade tracks scores: each row is a player and each column is a round. The same grid has two useful totals. 

Type the technique in `main.py`, press Run to inspect the result, then Submit.

## Your Task

1. Implement `totals(scores)` with `np.sum` along both axes, returning round totals first and player totals second.
