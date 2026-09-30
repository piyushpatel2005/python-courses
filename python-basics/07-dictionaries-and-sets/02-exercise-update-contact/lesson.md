---
title: 'Exercise: Update a Contact'
slug: exercise-update-contact
order: 2
language: python
lesson_type: coding
runtime: pyodide
summary: Read, update, and safely look up Python dictionary fields.
seo_title: 'Exercise: Update a Contact | Python Basics'
seo_description: Read, update, and safely look up Python dictionary fields with an
  editable Python example and checked task.
seo_keywords:
- python dictionary-fields
- beginner dictionary-fields exercise
---

The library contact card has named fields. Transfer the stock-card pattern to this contact: access a known key with brackets, change a field with assignment, and use `get` for an absent key.

This is a separate exercise. Edit `main.py`, press **Run** to inspect the output, then **Submit** to check the numbered tasks.

Keep the supplied card. Run to inspect all three results and Submit.

## Your Tasks

1. Set `visitor` to the value under `name` in `contact`.
2. Update `contact["visits"]` to `3`.
3. Set `phone` with `contact.get("phone", "not provided")`.
