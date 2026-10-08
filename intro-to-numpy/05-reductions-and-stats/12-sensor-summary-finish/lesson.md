---
title: "Project: flag variability"
slug: sensor-summary-finish
order: 12
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Project: flag variability with NumPy arrays."
seo_title: "Project: flag variability | Intro to NumPy"
seo_description: "Practice project: flag variability in a runnable NumPy lesson."
seo_keywords: [numpy, arrays, statistics]
hints:
  - Read the shape of the input and the requested result before choosing an axis.
---

Continue the same panel report from the previous lesson. The starter already includes your completed `panel_basics` function and the same night-by-sensor grid. Add median per night, which resists an unusually bright reading, and standard deviation per sensor to show which instrument fluctuates.

Type the technique in `main.py`, press Run to inspect the result, then Submit.

## Your Task

1. Implement `panel_variability(grid)` using row medians and column standard deviations.
