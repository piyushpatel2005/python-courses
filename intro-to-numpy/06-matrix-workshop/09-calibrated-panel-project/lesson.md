---
title: "Project: calibrate the panel"
slug: calibrated-panel-project
order: 9
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Project: calibrate the panel with NumPy arrays."
seo_title: "Project: calibrate the panel | Intro to NumPy"
seo_description: "Practice project: calibrate the panel in a runnable NumPy lesson."
seo_keywords: [numpy, arrays, matrices]
hints:
  - Read the shape of the input and the requested result before choosing an axis.
---

Apply a shared calibration matrix to every night’s sensor readings. Then put derived channels in rows for a technician who scans one channel at a time. 

Type the technique in `main.py`, press Run to inspect the result, then Submit.

## Your Task

1. Implement `calibrated_channels(grid, calibration)` by matrix-multiplying, then transposing the result.
