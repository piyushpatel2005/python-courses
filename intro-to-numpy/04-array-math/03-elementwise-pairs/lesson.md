---
title: Combine matching readings
slug: elementwise-pairs
order: 3
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: "Add arrays by pairing readings at matching positions."
seo_title: Combine matching readings | NumPy
seo_description: "Add arrays by pairing readings at matching positions."
seo_keywords:
  - NumPy
  - Python
  - elementwise pairs
hints:
  - 'Add matching positions; do not reduce the arrays to a total.'
---

Two instruments measure at the same times. Instead of combining an array with one scalar, you can combine two arrays of the same shape.

`a + b`, `a - b`, and `a * b` pair entries at matching positions. For example, the first result of `left + right` is `4 + 1`. `*` also works element by element; it is not matrix multiplication, which comes later.

## Your Task

1. Change subtraction to addition in `combined`.

Run `main.py` to see `[5 10 15]`, then Submit.
