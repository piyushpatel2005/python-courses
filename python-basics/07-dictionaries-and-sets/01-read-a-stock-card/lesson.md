---
title: 'Read an Atlas Map Card'
slug: read-a-stock-card
order: 1
language: python
lesson_type: coding
runtime: pyodide
summary: 'Read keyed landmarks and update marks in an atlas dictionary.'
seo_title: 'Read an Atlas Map Card | Python Basics'
seo_description: 'Read keyed landmarks and update marks in an atlas dictionary.'
seo_keywords:
- python dictionary-fields
- beginner dictionary-fields exercise
---

In the Map Archive, a dictionary gives each field a name. You can look up a landmark without remembering which position holds it.

`map_card["landmark"]` reads a value by its key. An assignment to `map_card["marks"]` updates that field. If a key is missing, bracket lookup raises `KeyError`; `map_card.get("route", "unknown")` returns the fallback instead.

![Map card key-to-value lookup and missing-key fallback](dictionary-lookup.svg)

Edit `main.py` so the first line reads the landmark. Run should print `lens` instead of `4`; the supplied later lines still show `Marks: 9` and `Route: unknown`. Then Submit.

## Your Task

1. Read `map_card["landmark"]` into `landmark`.
