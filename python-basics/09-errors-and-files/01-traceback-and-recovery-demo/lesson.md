---
title: 'Recover from a bad quantity'
slug: traceback-and-recovery-demo
order: 1
language: python
lesson_type: coding
runtime: pyodide
summary: 'Catch ValueError when a receipt quantity is not a number.'
seo_title: 'Recover from a bad quantity | Python Basics'
seo_description: 'Catch ValueError when a receipt quantity is not a number.'
seo_keywords: [python traceback, ValueError, try except]
---

A receipt has a quantity stored as text. `int("4")` gives the number `4`, but `int("unknown")` raises a `ValueError`. Without a handler, Python stops and shows a traceback pointing to the failed conversion.

The starter already uses `try` for the conversion and `except ValueError` for the fallback. A valid quantity returns from `try`; only invalid integer text reaches `except`. Change the fallback to `-1` to mark a quantity that needs correction. Keep the conversion intact.

## Your Task

1. Change the `ValueError` fallback in `safe_quantity(text)` to `-1`.

Edit `main.py` and press **Run**. You should see `Quantity: 4` and `Needs review: -1`. Then press **Submit**.
