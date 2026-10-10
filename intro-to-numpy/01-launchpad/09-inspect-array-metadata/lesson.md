---
title: Read shape and size
slug: inspect-array-metadata
order: 9
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Distinguish axes, total elements, and the length of the first axis.
seo_title: Read shape and size | NumPy for beginners
seo_description: Distinguish axes, total elements, and the length of the first axis.
seo_keywords:
  - NumPy
  - Python arrays
  - inspect array metadata
---

Before calculating with an array, check how its values are arranged. NumPy exposes that information through **attributes**: names after a dot, without parentheses.

| Expression | What it tells you |
| --- | --- |
| `pads.ndim` | Number of axes, or dimensions |
| `pads.shape` | Length of each axis, in order |
| `pads.size` | Total number of elements |
| `len(pads)` | Length of the first axis only |

An **axis** is one position in the shape tuple. For a grid, the first axis counts rows. For our frame stack, it counts frames instead.

Run the starter. Its output is `2 (2, 2) 4 2`: two axes, a two-by-two shape, four values, and a first-axis length of two.

## Your Task

1. Make `pads` a stack containing the existing `[[2, 4], [6, 8]]` frame followed by `[[10, 12], [14, 16]]`.

Run again to see `3 (2, 2, 2) 8 2`. There are now three axes and eight values. `len(pads)` is still two, but it now counts frames, not rows. Submit to check your stack.
