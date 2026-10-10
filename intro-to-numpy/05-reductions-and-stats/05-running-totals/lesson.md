---
title: "Keep a running tally"
slug: running-totals
order: 5
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Keep the cumulative sighting count after each interval."
seo_title: "Keep a running tally | Intro to NumPy"
seo_description: "Keep the cumulative sighting count after each interval."
seo_keywords: [numpy, arrays, statistics]
hints:
  - '`cumsum` keeps intermediate totals instead of only the last one.'
---

The telescope counts sightings in successive intervals. A sum tells you the final count; `np.cumsum` keeps the count after each interval.

For `[3, 1, 4, 2]`, the running totals are `3`, `3 + 1`, `3 + 1 + 4`, and `3 + 1 + 4 + 2`. This 1D cumulative result has the same length as its input, unlike a single total.

## Your Task

1. Replace `np.sum` with `np.cumsum` in `running`.

Run `main.py` to see `[3 4 8 10]`, then Submit.
