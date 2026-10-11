---
title: Find a usable band
slug: logical-comparisons
order: 5
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: "Combine inclusive bounds into a boolean mask and check the whole result."
seo_title: Find a usable band | NumPy
seo_description: "Combine inclusive bounds into a boolean mask and check the whole result."
seo_keywords:
  - NumPy
  - Python
  - logical comparisons
hints:
  - 'Keep parentheses around both comparisons when you join them with `&`.'
---

The boolean masks you used for filtering can also combine several conditions. This detector accepts a reading only when it meets both bounds.

Use `(bands >= 5) & (bands <= 10)` for an inclusive range. Each comparison needs parentheses. `&` means elementwise AND; `|` means elementwise OR. Python's `and` and `or` do not combine array masks.

`np.array_equal(a, b)` answers a different question: it returns one boolean saying whether two arrays have the same shape and values. The supplied print calls let you compare the mask with its expected pattern.

## Your Task

1. Change the upper bound in `usable` from `7` to `10`.

Run `main.py`: the mask should be `[False  True  True False]` and the whole-array check should be `True`. Then Submit.
