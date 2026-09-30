---
title: Look Up and Update a Dictionary
slug: read-a-stock-card
order: 1
language: python
lesson_type: coding
runtime: pyodide
summary: Read and update named fields in a Python dictionary.
seo_title: Look Up and Update a Dictionary | Python Basics
seo_description: Read and update named fields in a Python dictionary with an editable
  Python example and checked task.
seo_keywords:
- python dictionary-fields
- beginner dictionary-fields exercise
---

A dictionary stores `key: value` pairs. A key such as `"item"` identifies a field instead of an index. `card["item"]` reads it; `card["qty"] = 9` updates it. Missing keys raise `KeyError`; `card.get("aisle", "unknown")` supplies a fallback.

This is an editable worked demo. Edit `main.py`, press **Run** to compare the result, then **Submit** to check your small change. The next lesson transfers the idea to a different setting.

Change `item` to read the name, not the quantity. Run should print `paper`; then Submit.

## Your Task

1. Read `card["item"]` into `item`.
