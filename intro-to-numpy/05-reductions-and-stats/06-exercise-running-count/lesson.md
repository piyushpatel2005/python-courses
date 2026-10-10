---
title: "Build an interval counter"
slug: exercise-running-count
order: 6
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Return the visitor count reached by the end of each hour."
seo_title: "Build an interval counter | Intro to NumPy"
seo_description: "Return the visitor count reached by the end of each hour."
seo_keywords: [numpy, arrays, statistics]
hints:
  - 'Keep the input order; cumulative counting does not sort the values.'
---

A door sensor counts visitors per hour. The cumulative array should show how many have arrived by the end of each hour, in the original order.

## Your Task

1. In `running_count`, return `np.cumsum(counts)`.

Edit `main.py`, Run to check `[2 7 8]`, then Submit. An hour with zero visitors should repeat the previous running total rather than reset it.
