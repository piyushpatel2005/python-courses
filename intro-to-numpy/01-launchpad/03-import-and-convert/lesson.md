---
title: Turn a list into an array
slug: import-and-convert
order: 3
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Import NumPy and convert a small signal list to an ndarray.
seo_title: Turn a list into an array | NumPy for beginners
seo_description: Import NumPy and convert a small signal list to an ndarray.
seo_keywords:
  - NumPy
  - Python arrays
  - import and convert
---

The arcade scoreboard has three scores. The line `np.array([4, 6, 9])` starts with a Python list and creates a NumPy array containing those values.

The list goes inside square brackets; the function call goes inside parentheses. Keep both pairs as you edit. `print(scores.tolist())` converts the array back to a list just for display.

Run the starter in `main.py`. It prints `[4, 6, 9]`.

## Your Task

1. Change the last score from `9` to `12` inside `np.array(...)`.

Leave the first two scores unchanged. Run again to see `[4, 6, 12]`, then Submit. The next exercise will accept a supplied list rather than use a fixed scoreboard.
