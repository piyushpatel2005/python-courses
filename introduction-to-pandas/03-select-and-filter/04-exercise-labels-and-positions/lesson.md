---
title: "Exercise: inspect two delivery windows"
slug: exercise-labels-and-positions
order: 4
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Write label and position selectors that accept changing slice boundaries."
seo_title: "Exercise: inspect two delivery windows | Introduction to Pandas"
seo_description: "Write label and position selectors that accept changing slice boundaries."
seo_keywords: [pandas, python, data selection]
---

A delivery list has labels `dawn`, `noon`, and `night`. Reuse the preceding window pattern on this different list. Keep the original index in your answers. The column order matters in the label window; the positional window uses the first two columns.

## Your Tasks

1. Return rows from `start` through `stop`, inclusive, with `item` and `count` in `label_window(frame, start, stop)`.
2. Return rows from position `start` up to but not including `stop`, and the first two columns, in `position_window(frame, start, stop)`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
