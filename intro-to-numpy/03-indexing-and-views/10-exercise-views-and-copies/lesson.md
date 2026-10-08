---
title: 'Exercise: preserve a calibration snapshot'
slug: exercise-views-and-copies
order: 10
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: A new instrument must expose a live middle window and a safe snapshot of
  the same span.
seo_title: 'Exercise: preserve a calibration snapshot | NumPy'
seo_description: A new instrument must expose a live middle window and a safe snapshot
  of the same span. Practice NumPy in the browser.
seo_keywords:
  - NumPy
  - Python
  - views and copies
hints:
  - Make the copy before editing the view; check `np.shares_memory` in the test results.
---

A new instrument must expose a live middle window and a safe snapshot of the same span.

Use the preceding editable example as a pattern, but solve this new data task in `main.py`.

## Your Tasks

1. In `calibrate(record)`, create a middle-two-item slice view and an independent copy of that slice. Change their first entries to `50` and `-5` respectively, then return `(view, snapshot)`.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check each task.
