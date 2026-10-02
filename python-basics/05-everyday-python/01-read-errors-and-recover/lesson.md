---
title: Read Errors and Recover
slug: read-errors-and-recover
order: 1
language: python
lesson_type: coding
runtime: pyodide
summary: Read a traceback and recover from invalid beacon energy values.
seo_title: Python Errors and try/except | Python Basics
seo_description: Handle invalid energy text in The Lantern Atlas with try and except ValueError.
seo_keywords: [python errors, traceback, try except, ValueError]
hints:
  - Put int(text) inside try and return 0 in except ValueError.
---

# Recover a beacon reading

At the save shrine, Ari finds an energy reading stored as text. Some readings say `"unknown"` instead of `"3"`. Return zero for unreadable readings so one bad inscription does not stop the journey.

A traceback points to the failed line and ends with an error name. `int("unknown")` raises `ValueError`; accessing a missing list index raises `IndexError`; a misspelled name raises `NameError`. A `SyntaxError` means Python cannot parse the code at all. Read the last line of a traceback, then inspect the indicated line.

Protect only the operation that might fail:

```python
try:
    flame = int("dim")
except ValueError:
    flame = 0
print(flame)  # 0
```

`except ValueError` does not hide unrelated mistakes. Run `main.py`: both sample results initially say `None`. Your change should display `3` and `0`.

## Your Task

1. Complete `parse_energy(text)` so valid integer text returns an `int`, and text that raises `ValueError` returns `0` using `try` / `except ValueError`. Run and Submit.
