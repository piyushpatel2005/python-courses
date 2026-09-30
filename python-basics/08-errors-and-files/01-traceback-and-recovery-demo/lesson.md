---
title: Tracebacks and a Safe Count Demo
slug: traceback-and-recovery-demo
order: 1
language: python
lesson_type: coding
runtime: pyodide
summary: Read a traceback and edit a try/except fallback for a changing count.
seo_title: "Tracebacks and a Safe Count Demo | Python Basics"
seo_description: Read a traceback and edit a try/except fallback for a changing count.
seo_keywords: [python traceback, ValueError, try except]
---

The supply desk receives a count as text. A traceback ending in `ValueError` tells you that `int("unknown")` could not convert it. Read the final line for the error type, then the indicated line for the failing operation; a `SyntaxError` must be repaired before the program can run.

The complete `safe_count` function catches **only** `ValueError`; unrelated errors should still surface. Edit `main.py`: change the fallback for invalid text from `0` to `-1`. Press Run to see `-1` for `"unknown"`, then Submit. The next lesson transfers this pattern to ticket quantities.

## Your Task

1. Change only the `ValueError` fallback to `-1`; valid numeric text must still become an integer.
