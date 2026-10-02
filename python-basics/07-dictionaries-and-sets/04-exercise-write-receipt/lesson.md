---
title: 'Exercise: Count Cache Marks'
slug: exercise-write-receipt
order: 4
language: python
lesson_type: coding
runtime: pyodide
summary: 'Build cache labels and sum marks from a dictionary.'
seo_title: 'Exercise: Count Cache Marks | Python Basics'
seo_description: 'Build cache labels and sum marks from a dictionary.'
seo_keywords:
- python dictionary-loop
- beginner dictionary-loop exercise
---

Ari needs a cache ledger. The earlier map demo collected keys; here each entry becomes a label, and the marks become a total. Use `.items()` for pairs and `.values()` for just the counts.

Edit `main.py`, **Run** to see the labels and sum, then **Submit**.

## Your Tasks

1. Loop over `caches.items()` and append each `<landmark>: <marks> marks` label to `lines`.
2. Loop over `caches.values()` and add each count to `total_marks`.
