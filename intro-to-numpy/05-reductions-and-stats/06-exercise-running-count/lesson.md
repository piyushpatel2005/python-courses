---
title: "Build an interval counter"
slug: exercise-running-count
order: 6
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Build an interval counter with NumPy arrays."
seo_title: "Build an interval counter | Intro to NumPy"
seo_description: "Practice build an interval counter in a runnable NumPy lesson."
seo_keywords: [numpy, arrays, statistics]
hints:
  - Read the shape of the input and the requested result before choosing an axis.
---

A door sensor counts visitors per hour. The cumulative array reveals the count after each hour. 

Type the technique in `main.py`, press Run to inspect the result, then Submit.

## Your Task

1. Implement `running_count(counts)` with `np.cumsum`.
