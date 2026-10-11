---
title: "Choose an axis"
slug: sum-across-axes
order: 3
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Choose which grid dimension to reduce for night or sensor totals."
seo_title: "Choose an axis | Intro to NumPy"
seo_description: "Choose which grid dimension to reduce for night or sensor totals."
seo_keywords: [numpy, arrays, statistics]
hints:
  - 'For one result per night, reduce across that night’s sensor columns.'
---

A grid has rows for nights and columns for sensors. With no `axis` argument, `np.sum(grid)` adds every cell into one total. An axis lets you keep separate totals for one dimension.

For shape `(2, 3)`, axis 0 is the two-row dimension and axis 1 is the three-column dimension. A reduction removes the dimension you name:

- `axis=0` adds down the nights, leaving three sensor totals, shape `(3,)`.
- `axis=1` adds across the sensors, leaving two night totals, shape `(2,)`.

![Axis 0 gives sensor totals 6, 6, 9; axis 1 gives night totals 10, 11](axes-rows-columns.svg)

Read the first night across: `2 + 5 + 3` gives 10. That is one output per row, so it is the column dimension, axis 1, that disappears.

## Your Task

1. Change the axis in `night_totals` from `0` to `1`.

Run `main.py` to see `[10 11]`, then Submit.
