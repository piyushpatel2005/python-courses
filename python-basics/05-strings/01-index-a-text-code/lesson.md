---
title: Index a Text Code
slug: index-a-text-code
order: 1
language: python
lesson_type: coding
runtime: pyodide
summary: Indexing a Python string from either end.
seo_title: Index a Text Code | Python Basics
seo_description: Indexing a Python string from either end with an editable Python
  example and checked task.
seo_keywords:
- python indexing
- beginner indexing exercise
---

A volunteer reads a label code one character at a time. `code[0]` selects the first character; `code[-1]` selects the last. Indexes start at zero. `len(code)` counts characters. A single index beyond the end raises `IndexError`. Strings cannot be changed by assigning to an index.

This is an editable worked demo. Edit `main.py`, press **Run** to compare the result, then **Submit** to check your small change. The next lesson transfers the idea to a different setting.

Change `last` to select the final character of this different label. The visible result should be `R`; then Submit.

## Your Task

1. Set `last` to the last character of `code` using a negative index.
