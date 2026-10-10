---
title: Apply functions to a full array
slug: numpy-functions
order: 7
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: "Use NumPy functions on arrays of angles and positive values."
seo_title: Apply functions to a full array | NumPy
seo_description: "Use NumPy functions on arrays of angles and positive values."
seo_keywords:
  - NumPy
  - Python
  - numpy functions
hints:
  - 'The first output uses `wave`; the remaining print calls are supplied examples.'
---

An angle sensor needs a sine value for every angle. NumPy functions accept whole arrays, just as arithmetic operators do.

`np.sin` and `np.cos` take angles in **radians**: `np.pi / 2` is a quarter turn. The supplied `np.round(values, 3)` calls round the display to three decimal places, so tiny floating-point errors do not distract from the pattern.

The other print calls show a second pair of functions. `np.log` is the natural logarithm, and `np.e` is its base. For positive inputs, `np.exp` reverses the logarithm, apart from rounding error. Keep inputs modest: very large exponentials can overflow. A logarithm of zero produces a non-finite value and a warning with NumPy's default settings.

## Your Task

1. Change `np.cos` to `np.sin` in `wave`.

Run `main.py`: the first line becomes `[0. 1.]`. The logarithm and exponential examples stay unchanged. Then Submit.
