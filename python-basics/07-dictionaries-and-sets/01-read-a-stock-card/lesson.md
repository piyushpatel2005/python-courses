---
title: 'Read an Atlas Map Card'
slug: read-a-stock-map_card
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

Ari opens the Map Archive. Each map card has a named landmark and a count of marks. Dictionary keys let Ari retrieve a field without guessing its position. `map_card["landmark"]` reads a known key; assigning `map_card["marks"]` changes a value. An absent key raises `KeyError`, while `.get("route", "unknown")` gives a safe fallback.

![Map card key-to-value lookup and missing-key fallback](dictionary-lookup.svg)

Edit `main.py`, press **Run**, then **Submit**. The first line should change from `4` to `lens`; the later lines should show `Marks: 9` and `Route: unknown`. The next exercise uses a different map record.

## Your Task

1. Read `map_card["landmark"]` into `landmark`.
