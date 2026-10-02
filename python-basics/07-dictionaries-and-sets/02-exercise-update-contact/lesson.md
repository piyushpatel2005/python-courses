---
title: 'Exercise: Update a Map Entry'
slug: exercise-update-map_entry
order: 2
language: python
lesson_type: coding
runtime: pyodide
summary: 'Read, update, and safely look up fields in an atlas map entry.'
seo_title: 'Exercise: Update a Map Entry | Python Basics'
seo_description: 'Read, update, and safely look up fields in an atlas map entry.'
seo_keywords:
- python dictionary-fields
- beginner dictionary-fields exercise
---

Ari finds a map entry for Moss Gate. Transfer the card lookup pattern: read its landmark, record one more mark, and request an optional clue without raising `KeyError`.

Edit `main.py`, press **Run** to inspect the entry, then **Submit**.

## Your Tasks

1. Set `landmark` from `map_entry["landmark"]`.
2. Update `map_entry["marks"]` to `3`.
3. Set `clue` using `map_entry.get("clue", "unmarked")`.
