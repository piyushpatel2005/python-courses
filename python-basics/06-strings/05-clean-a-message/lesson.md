---
title: "Clean a Meeting Message: Demo"
slug: clean-a-message
order: 5
language: python
runtime: pyodide
lesson_type: coding
summary: Remove surrounding whitespace and lowercase a meeting update.
seo_title: "Clean a Meeting Message: Demo | Python Basics"
seo_description: Remove surrounding whitespace and lowercase a meeting update.
seo_keywords: [python basics, strings, strip, lower, text messages]
---

# Clean a meeting message

A meeting update arrives as `"  Meeting Delayed  "`. Those surrounding spaces and capital letters make a direct text comparison unreliable.

A string **method** is called with a dot after a string:

- `strip()` removes whitespace at the beginning and end.
- `lower()` converts uppercase letters to lowercase.

You can chain them: `message.strip().lower()` strips first, then lowercases the result. The original `message` stays unchanged.

## Your Task

1. Set `cleaned` to `message` without surrounding whitespace and with lowercase letters.

The `.strip()` call is supplied in `main.py`. Add the remaining method, Run to see `meeting delayed`, then Submit.

Two more methods help with the next notice. `replace(old, new)` returns a copy with matching text replaced; `startswith(prefix)` reports `True` or `False`.

```python run
status = "door closed"
print(status.replace("closed", "open"))
print(status.startswith("door"))
print(status)
```

Run this separate example to see `door open`, `True`, then the unchanged `door closed`.
