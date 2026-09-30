---
title: Read Errors and Recover
slug: read-errors-and-recover
order: 1
language: python
lesson_type: coding
runtime: pyodide
summary: Read a Python traceback and recover from invalid workshop seat counts.
seo_title: Python Errors and try/except | Python Basics
seo_description: Learn to identify Python error names and use try/except to handle invalid workshop registration counts.
seo_keywords: [python errors, traceback, try except, ValueError]
hints:
  - Put int(text) inside try and return 0 in except ValueError.
---

The workshop sign-up sheet has a seat count stored as text. Some entries say `"three"` instead of `"3"`. Rather than let one entry stop the report, you can return a safe count of zero.

A traceback points to the line that failed and ends with an error name. `int("three")` raises `ValueError` because the text is not a valid integer. `numbers[8]` on a three-item list raises `IndexError`. A misspelled variable often raises `NameError`. A `SyntaxError` means Python could not parse the program; repair the code before it can run. Read the last line of a traceback, then inspect the indicated line.

This short example protects only the operation that might fail:

```python
try:
    shelf = int("unknown")
except ValueError:
    shelf = 0
print(shelf)  # 0
```

`except ValueError` handles that specific error; it does not hide unrelated mistakes. Run the starter: its example labels still say `None`. After your change, valid counts show their integer values and invalid counts show `0`.

## Your Task

1. Complete `parse_seats(text)` so valid integer text returns an `int`, and text that raises `ValueError` returns `0` using `try`/`except ValueError`.
