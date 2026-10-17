---
title: "Clean a Rune Message: Demo"
slug: clean-a-message
order: 5
language: python
lesson_type: coding
runtime: pyodide
summary: Normalize a rune message with strip and lower.
seo_title: "Clean a Rune Message: Demo | Python Basics"
seo_description: Normalize a rune message with strip and lower.
seo_keywords: [python basics, strings, lantern atlas]
---

# Clean a Rune Message: Demo

A message can contain the right words but still be awkward to compare: `"  Beacon Dim  "` has extra spaces and mixed capitalization.

A string **method** is an operation called after the string, using a dot. Here are two that help:

- `strip()` removes whitespace from the beginning and end.
- `lower()` turns uppercase letters into lowercase letters.

You can chain them. In `message.strip().lower()`, Python strips the spaces first, then lowercases that result. It doesn't change the original `message`.

## Your Task

1. Set `cleaned` to `message` with its surrounding whitespace removed and its letters lowercased.

In `main.py`, the `.strip()` call is already supplied. Add the remaining method, Run to see `beacon dim`, then Submit.

Two more methods will help with the next notice. `replace(old, new)` returns a string with matching text replaced; `startswith(prefix)` returns `True` or `False`.

```python run
status = "gate closed"
print(status.replace("closed", "open"))
print(status.startswith("gate"))
print(status)
```

Run this example to see `gate open`, `True`, and the unchanged `gate closed`. Replacing text creates a new string; it doesn't rewrite `status`.
