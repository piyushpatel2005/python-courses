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

Before reading a sound board, check its layout. `ndim` counts axes; `shape` lists their lengths; `size` counts all values; `len` measures only the first axis. In a 3D stack, `len` counts frames, not all cells.

Edit `main.py` to turn the existing 2D board into the first frame of a stack and add a second frame. Press **Run**: `ndim` rises from 2 to 3 and `size` doubles, while `len` stays 2 because the new first axis contains two frames. Then **Submit**.

## Your Task

1. Make `pads` a stack containing the existing `[[2, 4], [6, 8]]` frame followed by `[[10, 12], [14, 16]]`.
