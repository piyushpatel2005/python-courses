---
title: "Describe a series"
slug: describe-a-series
order: 7
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Describe center and spread with mean, median, variance, and standard deviation."
seo_title: "Describe a series | Intro to NumPy"
seo_description: "Describe center and spread with mean, median, variance, and standard deviation."
seo_keywords: [numpy, arrays, statistics]
hints:
  - 'Use `np.std` with its default `ddof=0` for population spread.'
---

Two sensors can have the same average but fluctuate by different amounts. Use a measure of center alongside a measure of spread.

- `np.mean` adds the values and divides by their count.
- `np.median` finds the middle of the sorted values, or the average of the middle pair for an even count.
- `np.var` averages squared distances from the mean.
- `np.std` takes the square root of that variance, returning spread in the original units.

For `[10, 12, 14]`, the mean and median are 12. Distances from the mean are `[-2, 0, 2]`; their squares are `[4, 0, 4]`. Variance is `8 / 3`, and standard deviation is about `1.633`.

![The temperatures 10, 12, 14 have mean 12, variance 8 divided by 3, and standard deviation about 1.633](center-and-spread.svg)

NumPy defaults to `ddof=0`: divide by the number of readings. We use this **population** calculation to describe exactly the values supplied, rather than estimating spread for a larger population.

## Your Task

1. Change `np.mean` to `np.std` in `spread`.

Run `main.py` to see approximately `1.633`, then Submit.
