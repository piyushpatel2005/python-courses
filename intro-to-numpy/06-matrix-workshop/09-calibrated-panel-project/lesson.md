---
title: "Project: calibrate the panel"
slug: calibrated-panel-project
order: 9
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: 'Build on the matrix-product helper to display one calibrated channel per row.'
seo_title: "Project: calibrate the panel | Intro to NumPy"
seo_description: 'Build on the matrix-product helper to display one calibrated channel per row.'
seo_keywords: [numpy, arrays, matrices]
hints:
  - Call the supplied transform_panel helper, then transpose its result.
---

The Pocket Observatory needs a calibrated panel that a technician can scan one channel at a time. The starter carries forward the finished `transform_panel` function from the previous exercise. A new sample has two sensor channels and a calibration that produces three derived channels.

The supplied helper already returns nights in rows and derived channels in columns. Your change is to turn that result so each channel has its own row. For this sample, shape `(2, 3)` becomes `(3, 2)`.

Edit `calibrated_channels` in `main.py`. Run to inspect the channel rows, then Submit. Leave the supplied helper in place; the next lesson will build on both functions.

## Your Task

1. Implement `calibrated_channels(grid, calibration)` by transposing the result of the supplied `transform_panel` helper.
