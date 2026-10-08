---
title: "Find the loudest reading"
slug: find-extremes
order: 1
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Find the loudest reading with NumPy arrays."
seo_title: "Find the loudest reading | Intro to NumPy"
seo_description: "Practice find the loudest reading in a runnable NumPy lesson."
seo_keywords: [numpy, arrays, statistics]
hints:
  - Read the shape of the input and the requested result before choosing an axis.
---

An arcade sound meter recorded three moments. A reduction compresses the readings to one answer; `argmax` instead gives the zero-based position. `np.sum`, `np.min`, and `np.max` return values; `np.argmin` and `np.argmax` return positions. Ties choose the first position.

Run `main.py` first, make the small edit, then Submit.

## Your Task

1. Change `np.min` to `np.max` so the display shows 68.
