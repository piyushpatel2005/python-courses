---
title: "Compare center and spread"
slug: exercise-series-stats
order: 8
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Calculate four separate statistics for a series of readings."
seo_title: "Compare center and spread | Intro to NumPy"
seo_description: "Calculate four separate statistics for a series of readings."
seo_keywords: [numpy, arrays, statistics]
hints:
  - 'Mean and median can differ; calculate both from the supplied array.'
---

A sound meter sends a short series of readings. Give its report separate measures of center and spread.

Keep the starter's tuple return in place and fill its four placeholders. Use the default population calculations (`ddof=0`) for variance and standard deviation.

## Your Tasks

1. Set `mean` to `np.mean(readings)`.
2. Set `median` to `np.median(readings)`.
3. Set `variance` to `np.var(readings)`.
4. Set `std` to `np.std(readings)`.

Run `main.py` after each change, then Submit. The sample's mean and median both equal 44; another series need not have equal mean and median.
