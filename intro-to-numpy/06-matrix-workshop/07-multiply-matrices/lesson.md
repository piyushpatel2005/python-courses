---
title: "Combine matrix dimensions"
slug: multiply-matrices
order: 7
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Combine matrix dimensions with NumPy arrays."
seo_title: "Combine matrix dimensions | Intro to NumPy"
seo_description: "Practice combine matrix dimensions in a runnable NumPy lesson."
seo_keywords: [numpy, arrays, matrices]
hints:
  - Read the shape of the input and the requested result before choosing an axis.
---

A `(2, 3)` grid times a `(3, 2)` calibration matrix gives a `(2, 2)` output. Inner dimensions must match; output dimensions are the outer pair. `*` instead multiplies matching cells, not rows by columns. The first output cell combines the first grid row with the first calibration column: `1×1 + 2×0 + 3×1 = 4`. `grid * 2` only doubles each individual cell.

![A two-by-three measurement grid multiplied by a three-by-two calibration matrix produces a two-by-two derived grid; one output cell combines one row and one column](matrix-dot-product.svg)


Run `main.py` first, make the small edit, then Submit.

## Your Task

1. Replace the `combined` assignment with `grid @ calibration` and observe its `(2, 2)` shape.
