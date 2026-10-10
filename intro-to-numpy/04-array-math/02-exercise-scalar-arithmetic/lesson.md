---
title: 'Exercise: calibrate a pressure series'
slug: exercise-scalar-arithmetic
order: 2
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: "Write a pressure-calibration function that uses the supplied gain and offset."
seo_title: 'Exercise: calibrate a pressure series | NumPy'
seo_description: "Write a pressure-calibration function that uses the supplied gain and offset."
seo_keywords:
  - NumPy
  - Python
  - scalar arithmetic
hints:
  - 'Use the parameters rather than the numbers from the sample call.'
---

A barometer uses a gain and an offset to calibrate its pressure readings. Both settings are supplied to your function, so the same calculation can work with another instrument.

The starter includes the function and a print call. Replace `return None`; leave the original array unchanged.

## Your Task

1. In `calibrate_pressure`, return a new array calculated as `raw * gain + offset`.

Run `main.py` to check the sample: `[7 13 19]`. Submit when it is ready.
