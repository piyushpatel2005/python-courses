---
title: "Keep a running tally"
slug: running-totals
order: 5
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Keep a running tally with NumPy arrays."
seo_title: "Keep a running tally | Intro to NumPy"
seo_description: "Practice keep a running tally in a runnable NumPy lesson."
seo_keywords: [numpy, arrays, statistics]
hints:
  - Read the shape of the input and the requested result before choosing an axis.
---

The telescope counts sightings in successive intervals. `cumsum` keeps every intermediate total instead of only the final sum. 

Run `main.py` first, make the small edit, then Submit.

## Your Task

1. Replace `np.sum` with `np.cumsum` to show `[3 4 8 10]`.
