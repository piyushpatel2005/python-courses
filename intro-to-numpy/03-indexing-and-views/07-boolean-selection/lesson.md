---
title: Mark noisy readings
slug: boolean-selection
order: 7
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: A comparison such as `readings > 20` returns a boolean array.
seo_title: Mark noisy readings | NumPy
seo_description: A comparison such as `readings > 20` returns a boolean array. Practice
  NumPy in the browser.
seo_keywords:
  - NumPy
  - Python
  - boolean selection
hints:
  - Select with `cleaned[cleaned < threshold]` on the left side of `=`.
---

A sensor flags any reading beyond a safe limit.

A comparison such as `readings > 20` returns a boolean array. Use it inside brackets to select matching values or on the left of `=` to replace them. The mask must match the readings shape.

## Your Task

1. Change the replacement value to `0`; Run shows the two flagged readings cleared.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check the change.
