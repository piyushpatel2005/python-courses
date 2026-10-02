---
title: "Read a Rune Code: Demo"
slug: index-a-text-code
order: 1
language: python
lesson_type: coding
runtime: pyodide
summary: Index the first and last symbols of a cavern rune code.
seo_title: "Read a Rune Code: Demo | Python Basics"
seo_description: Index the first and last symbols of a cavern rune code.
seo_keywords: [python basics, strings, lantern atlas]
---

# Read a Rune Code: Demo

Ari carries the workshop loadout into Cipher Caverns. Route signs are strings; `code[0]` reads the first symbol and `code[-1]` the last. Indexes start at zero, and `len(code)` counts characters. A missing single index raises `IndexError`; strings cannot be changed by index.

Edit `last` in `main.py` to use a negative index. Run should show `N R`, then Submit. The next sign uses a different code.

## Your Task

1. Set `last` to the last character of `code` using a negative index.
