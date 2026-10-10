---
title: 'Exercise: Decode a sensor feed'
slug: exercise-import-and-convert
order: 4
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Write a reusable conversion function for incoming sensor lists.
seo_title: 'Exercise: Decode a sensor feed | NumPy for beginners'
seo_description: Write a reusable conversion function for incoming sensor lists.
seo_keywords:
  - NumPy
  - Python arrays
  - exercise import and convert
---

A station sends its readings as a Python list. Write a small function that converts whichever list it receives into a NumPy array.

The parameter `values` holds the incoming list. Use it in the conversion rather than writing the sample numbers inside the function. The supplied print call lets you check the result.

## Your Tasks

1. Make `make_feed(values)` return a NumPy array containing the supplied values.

Replace `return None` in `main.py`. Run should show `[11 14 17]` instead of `None`, then Submit checks another feed too.

NumPy's usual array display separates these values with spaces, not commas. That's a display difference, not a missing value. The original Python list remains a list.
