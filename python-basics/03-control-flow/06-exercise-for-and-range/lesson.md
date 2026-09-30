---
title: 'Exercise: Mark bus stops'
slug: exercise-for-and-range
order: 6
language: python
runtime: pyodide
lesson_type: coding
summary: Generate even-numbered bus stop labels with range.
seo_title: 'Exercise: Mark bus stops | Python Basics'
seo_description: Generate even-numbered bus stop labels with range. Practice Python
  control flow in an editable browser lesson.
seo_keywords:
- python for exercise
- range step
- numbered labels
---

# Exercise: Mark bus stops

The stall example increased the stop bound. A shuttle marks **even-numbered** bus stops instead. Use the three-argument form `range(start, stop, step)`; the stop number is not included. The supplied print shows the full label string.

Edit **main.py**, press **Run** to see `Stop 2 | Stop 4 | Stop 6 | `, then press **Submit**.

## Your Task

1. Use a `for` loop and `range(2, 8, 2)` to append `f"Stop {stop} | "` to `labels` for stops 2, 4, and 6. The supplied print line should show all three.
