---
title: "Transform a whole panel"
slug: exercise-transform-grid
order: 8
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: 'Transform a panel into derived channels using matrix multiplication.'
seo_title: "Transform a whole panel | Intro to NumPy"
seo_description: 'Transform a panel into derived channels using matrix multiplication.'
seo_keywords: [numpy, arrays, matrices]
hints:
  - Match grid columns to calibration rows before applying @.
---

Now apply the calibration idea to a different panel. Each row contains one night's three sensor readings. Each calibration column describes one derived channel, so the result will have one row per night and two columns.

Return the matrix product of the supplied parameters. Keep their order: `grid` comes first, then `calibration`. The sample's first night should become `[12 7]`.

Edit `main.py`, Run to inspect both nights, then Submit. The tests also use arrays with different shapes whose inner dimensions still match.

## Your Task

1. Implement `transform_panel(grid, calibration)` with matrix multiplication, not elementwise `*`.
