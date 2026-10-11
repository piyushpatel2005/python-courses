---
title: Scale every reading
slug: scalar-arithmetic
order: 1
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: "Apply one gain and offset to every reading while keeping the raw array unchanged."
seo_title: Scale every reading | NumPy
seo_description: "Apply one gain and offset to every reading while keeping the raw array unchanged."
seo_keywords:
  - NumPy
  - Python
  - scalar arithmetic
hints:
  - 'Multiplication happens before addition in `raw * 2 + offset`.'
---

You have selected readings with slices. Now correct a whole temperature series without changing the raw record.

A **scalar** is one number. In `raw * 2 + 1`, NumPy doubles every element, then adds 1 to each result. This makes a new array, unlike editing a slice view in the previous section.

## Your Task

1. Change the offset in `corrected` from `1` to `4`.

Edit `main.py`, then Run: `[10 14 18]` should appear. Submit to check your change.
