---
title: Choose and convert element types
slug: dtypes-and-astype
order: 9
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Inspect dtype families and convert numeric readings to Boolean, text, or
  complex.
seo_title: Choose and convert element types | NumPy for beginners
seo_description: Inspect dtype families and convert numeric readings to Boolean, text,
  or complex.
seo_keywords:
  - NumPy
  - Python arrays
  - dtypes and astype
---

The sound board turns levels into on/off flags. An array has one `dtype` for all elements: converting integers with `astype(bool)` makes zeros `False` and nonzero values `True`. By default, `astype` returns a new array, leaving the original alone.

You can also convert numbers to text with `astype(str)` or complex numbers with `astype(complex)`. `dtype.kind` identifies these families as `b` (Boolean), `U` (Unicode text), and `c` (complex), without depending on numeric widths. Integer arrays usually have kind `i`, and floating-point arrays have kind `f`.

A complex number has a real part and an imaginary part, written with `j` in Python: converting `5` produces `5+0j`. You only need to recognize that conversion here, not do complex arithmetic. To choose a type at creation rather than afterward, pass `dtype`, as in `np.array([1, 2], dtype=float)`.

Edit `main.py`, press **Run** to see the middle flag switch from `True` to `False` while the original array's type remains numeric, then **Submit**.

## Your Task

1. Change the middle sound-board level from 2 to 0 so its Boolean flag is off.
