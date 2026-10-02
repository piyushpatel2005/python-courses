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

At the Save Shrine, Ari reads a beacon charge written as text. `int(text)` converts digits but raises `ValueError` for `"faded"`. Catch that specific error so an unexpected bug is not silently hidden.

Edit `main.py` to change only the invalid-reading fallback from `0` to `-1`. Press **Run** to see `4` and `-1`, then **Submit**.

## Your Task

1. Change only the `ValueError` fallback to `-1`; numeric text must still convert.
