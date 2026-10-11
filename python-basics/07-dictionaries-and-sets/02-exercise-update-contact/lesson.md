---
title: 'Exercise: Update a Map Entry'
slug: exercise-update-contact
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

The Moss Gate entry needs one more mark. Use the dictionary keys to read its landmark and update its count. Its clue is optional, so use `get()` to supply a fallback when that key is absent.

Make the changes in `main.py`. Run to inspect the three results, then Submit.

## Your Tasks

1. Set `landmark` from `map_entry["landmark"]`.
2. Update `map_entry["marks"]` to `3`.
3. Set `clue` using `map_entry.get("clue", "unmarked")`.
