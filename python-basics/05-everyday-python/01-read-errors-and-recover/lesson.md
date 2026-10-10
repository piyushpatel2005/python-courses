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

At the save shrine, Adi finds an energy reading stored as text. A reading of `"3"` can become a number, but `"unknown"` cannot. You'll give the game a fallback value of zero when a reading is unreadable.

When Python stops with an error, start at the last line of the traceback. It names the error and explains what went wrong. Then look at the line of code it points to.

The error name helps narrow your search:

- `ValueError`: a value cannot be used as requested, as with `int("unknown")`.
- `IndexError`: a list index is out of range.
- `NameError`: Python cannot find a name, perhaps because it was misspelled.

A `SyntaxError` is different: Python cannot read the code as valid Python, so it cannot begin running it.

For the unreadable energy, put the conversion inside `try` and handle `ValueError` in `except`:

```python
try:
    flame = int("dim")
except ValueError:
    flame = 0
print(flame)  # 0
```

Python tries the conversion first. If it fails with `ValueError`, the `except` block sets `flame` to zero. Other kinds of errors still surface, so you can find and fix them.

Edit `main.py`. The supplied print calls currently show `None` because the function has no return value. After your change, Run should show `Valid energy: 3` and `Invalid energy: 0`. Use Submit to check the function with other readings too.

## Your Task

1. Complete `parse_energy(text)` using `try` / `except ValueError`: return the integer from `int(text)`, or `0` if the conversion fails.
