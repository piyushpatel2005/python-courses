---
title: 'Recover a Faded Beacon Reading'
slug: traceback-and-recovery-demo
order: 1
language: python
lesson_type: coding
runtime: pyodide
summary: 'Catch ValueError when a shrine reading is not numeric.'
seo_title: 'Recover a Faded Beacon Reading | Python Basics'
seo_description: 'Catch ValueError when a shrine reading is not numeric.'
seo_keywords: [python traceback, ValueError, try except]
---

Some charge readings at the Save Shrine have faded. `int("4")` returns a number, but `int("faded")` raises `ValueError`. If nothing catches that error, Python stops and prints a traceback showing where it happened.

The starter catches this specific error. Python tries the conversion inside `try`. If conversion fails, it skips to `except ValueError` and returns the fallback. A valid reading never enters that `except` block.

Edit only the fallback in `main.py`. Run should print `4` for the valid reading and `-1` for the faded one. Submit to check both paths.

## Your Task

1. Change only the `ValueError` fallback to `-1`; numeric text must still convert.
