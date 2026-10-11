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
seo_description: Gather selected array positions in a chosen order, including positions counted from the end.
seo_keywords:
  - NumPy
  - Python
  - select readings
hints:
  - Index `2` selects the third item; the first stays at `0`.
---

A receiver stores five sky brightness samples in arrival order.

As with Python lists, index `0` is the first item and `-1` is the last. A single index, such as `samples[0]`, returns one value.

To gather several positions, put a list inside the array brackets. In `samples[[0, 2]]`, the inner brackets form the list of positions; the outer brackets select from `samples`. This is called **fancy indexing** (or advanced indexing). It preserves your requested order and returns a separate array. You will compare that copy with a slice view later.

## Your Task

1. Change the second requested index from `3` to `2` so Run prints `[12 15]`.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check the change.
