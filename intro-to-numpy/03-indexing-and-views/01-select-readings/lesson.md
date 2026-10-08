---
title: Pick readings by position
slug: select-readings
order: 1
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: Index `0` is the first item; negative indices count backward.
seo_title: Pick readings by position | NumPy
seo_description: Index `0` is the first item; negative indices count backward. Practice
  NumPy in the browser.
seo_keywords:
  - NumPy
  - Python
  - select readings
hints:
  - Index `2` selects the third item; the first stays at `0`.
---

A receiver stores five sky brightness samples in arrival order.

Index `0` is the first item; negative indices count backward. A list of indices such as `samples[[0, 2]]` gathers values in the order you request and creates a separate array.

## Your Task

1. Change the second requested index from `3` to `2` so Run prints `[12 15]`.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check the change.
