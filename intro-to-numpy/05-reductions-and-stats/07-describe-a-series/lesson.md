---
title: "Describe a series"
slug: describe-a-series
order: 7
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Describe a series with NumPy arrays."
seo_title: "Describe a series | Intro to NumPy"
seo_description: "Practice describe a series in a runnable NumPy lesson."
seo_keywords: [numpy, arrays, statistics]
hints:
  - Read the shape of the input and the requested result before choosing an axis.
---

A stable sensor should have little spread. Mean and median describe the center; variance and standard deviation describe spread. NumPy uses population variance by default (`ddof=0`). For `[10, 12, 14]`, the mean and median are 12. Variance is the average squared distance from 12; standard deviation is its square root.

Run `main.py` first, make the small edit, then Submit.

## Your Task

1. Change `np.mean` to `np.std` to show the population standard deviation.
