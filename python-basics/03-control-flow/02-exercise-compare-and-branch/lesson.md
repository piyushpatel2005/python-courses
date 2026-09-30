---
title: 'Exercise: Choose a shelf sign'
slug: exercise-compare-and-branch
order: 2
language: python
runtime: pyodide
lesson_type: coding
summary: Compare remaining library copies and choose a shelf sign.
seo_title: 'Exercise: Choose a shelf sign | Python Basics'
seo_description: Compare remaining library copies and choose a shelf sign. Practice
  Python control flow in an editable browser lesson.
seo_keywords:
- python comparison exercise
- python if elif else
- library stock
---

# Exercise: Choose a shelf sign

The garden forecast used temperature; now a library uses its remaining copies. The starter supplies `copies_left` and the print lines. First compute a boolean comparison. Then use it to select exactly one sign: no copies means `Unavailable`; fewer than three means `Almost gone`; otherwise `Available`. An `if` chain evaluates branches from top to bottom; always check zero first.

Edit **main.py**, press **Run** to see `True` and `Almost gone` on separate lines for two copies, then press **Submit** to check each task.

## Your Tasks

1. Set `low_stock` using the comparison `copies_left < 3`, so two copies prints `True`.
2. Replace the placeholder sign with an `if` / `elif` / `else` chain choosing `Unavailable` for zero copies, `Almost gone` when `low_stock` is true, and `Available` otherwise. The supplied print should say `Almost gone` for two copies.
