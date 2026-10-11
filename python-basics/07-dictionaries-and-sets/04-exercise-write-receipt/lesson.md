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

Make a small ledger for the cache map. Each key-value pair becomes a readable label; the numeric values also contribute to a total.

Use `caches.items()` in the label loop and `caches.values()` in the counting loop. The starter supplies the empty list and starting total. Edit `main.py`, Run to see both results, then Submit.

## Your Tasks

1. Loop over `caches.items()` and append each `<landmark>: <marks> marks` label to `lines`.
2. Loop over `caches.values()` and add each count to `total_marks`.
