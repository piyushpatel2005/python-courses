---
title: Reuse column offsets across rows
slug: row-broadcast
order: 9
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: "Reuse a one-dimensional array of column offsets across every grid row."
seo_title: Reuse column offsets across rows | NumPy
seo_description: "Reuse a one-dimensional array of column offsets across every grid row."
seo_keywords:
  - NumPy
  - Python
  - row broadcast
hints:
  - 'Align shapes from the right; the three offsets match the three columns.'
---

A sky grid needs a different correction for each column. You do not need to write a loop over its rows.

The grid has shape `(2, 3)` and `column_offset` has shape `(3,)`. **Broadcasting** compares shapes from the right. The final dimensions both have length 3; the missing leading dimension acts like length 1 and can expand to 2. NumPy reuses the offsets for both rows without requiring you to build a repeated array.

A `(3,)` array is one-dimensional, not a 2D row or column. Here it behaves like a row of three column offsets.

![The starter adds offsets 10, 20, 30 to both rows of the sky grid](broadcast-row-offsets.svg)

The diagram shows the starter's addition. Your edit subtracts the same offsets instead.

## Your Task

1. Change `+` to `-` in `adjusted`.

Run `main.py`: the first row becomes `[-9 -18 -27]` and the second `[-6 -15 -24]`. Then Submit.
