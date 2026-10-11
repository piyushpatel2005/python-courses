---
title: 'Exercise: flag an observation window'
slug: exercise-logical-comparisons
order: 6
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: "Build a window mask and compare it with an expected boolean array."
seo_title: 'Exercise: flag an observation window | NumPy'
seo_description: "Build a window mask and compare it with an expected boolean array."
seo_keywords:
  - NumPy
  - Python
  - logical comparisons
hints:
  - 'Build the mask first, then compare it with `expected` using `np.array_equal`.'
---

A telescope accepts measurements inside caller-supplied limits. Keep the lower and upper endpoints: a reading exactly on either limit is still usable.

The first function builds a mask. The second checks that mask against an expected array; it should return one boolean, not another mask. Finish the first task before using it in the second.

## Your Tasks

1. In `in_window`, return a boolean NumPy array for readings from `low` through `high`, using parenthesized comparisons joined by `&`.
2. In `matches_window`, use `np.array_equal` to compare the `in_window` result with `expected`.

Run `main.py` after each edit. The completed sample prints a mask, then `True`. Submit to check the two results separately.
