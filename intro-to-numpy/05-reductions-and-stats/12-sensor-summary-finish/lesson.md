---
title: "Project: flag variability"
slug: sensor-summary-finish
order: 12
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Extend the same panel report with night medians and sensor variability."
seo_title: "Project: flag variability | Intro to NumPy"
seo_description: "Extend the same panel report with night medians and sensor variability."
seo_keywords: [numpy, arrays, statistics]
hints:
  - 'Reuse the same axes as the previous step: 1 for nights, 0 for sensors.'
---

Continue the same panel report. The starter includes the completed `panel_basics` function and the same night-by-sensor grid; you do not need to rebuild that work.

Add a median for each night and a population standard deviation for each sensor. `np.median` and `np.std` use the same axis rule as sums and means. A night median is less affected than its mean by one unusually bright reading. A sensor's standard deviation describes how much its readings fluctuate across the recorded nights; it does not by itself establish that the instrument is faulty.

## Your Tasks

1. Set `night_medians` to the median of each row in `grid`.
2. Set `sensor_std` to the population standard deviation of each column in `grid`.

Run `main.py`, then Submit. The second line should contain medians `[4. 7.]` and standard deviations `[2. 1.5 2.5]`; the totals and means on the first line stay unchanged.

Your panel now reports totals, center, and spread without losing the original grid. Next, you will work with individual sensor histories and matrix operations.
