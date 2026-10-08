---
title: "Project: report calibrated peaks"
slug: calibrated-panel-finish
order: 10
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Project: report calibrated peaks with NumPy arrays."
seo_title: "Project: report calibrated peaks | Intro to NumPy"
seo_description: "Practice project: report calibrated peaks in a runnable NumPy lesson."
seo_keywords: [numpy, arrays, matrices]
hints:
  - Read the shape of the input and the requested result before choosing an axis.
---

Continue the calibrated panel from the previous lesson: its finished `calibrated_channels` function and sample grid are already in the starter. Add a peak reading for each derived channel. Before transposing, the transformed output has nights in rows; reduce down the night axis (`axis=0`) to retain one maximum per channel.

Type the technique in `main.py`, press Run to inspect the result, then Submit.

## Your Task

1. Implement `channel_peaks(grid, calibration)` using matrix multiplication followed by a column-wise maximum.
