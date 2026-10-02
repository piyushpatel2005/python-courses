---
title: "Index a Gear List: Demo"
slug: index-a-supply-list
order: 1
language: python
lesson_type: coding
runtime: pyodide
summary: Read the last item of Ari’s ordered gear list.
seo_title: "Index a Gear List: Demo | Python Basics"
seo_description: Read the last item of Ari’s ordered gear list.
seo_keywords: [python basics, lists and tuples, lantern atlas]
---

# Index a Gear List: Demo

Ari arrives at Inventory Ridge with a decoded route. A list keeps gear in order: index zero is first, `-1` is last, and `len(gear)` counts items. An index beyond the list raises `IndexError`.

![Positive and negative indexes on Ari's gear list](list-indexing.svg "First item at 0, last at -1")

Change `last_gear` in `main.py` to select the last item. Run should print `lens`, then Submit. The next exercise builds a different list.

## Your Task

1. Set `last_gear` to the last item of `gear`.
