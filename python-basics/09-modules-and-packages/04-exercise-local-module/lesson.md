---
title: 'Exercise: Import a Shrine Rule'
slug: exercise-local-module
order: 4
language: python
runtime: pyodide
lesson_type: coding
summary: 'Import a generated local helper and use it in a function.'
seo_title: 'Exercise: Import a Shrine Rule | Python Basics'
seo_description: 'Import a generated local helper and use it in a function.'
seo_keywords: [python basics, exercise local module, python practice]
hints:
  - Use from shrine_rules import seal_count; then call seal_count(runes).
---

Ari needs seals for shrine runes. The supplied setup writes `shrine_rules.py` in the temporary browser filesystem; it defines `seal_count` for groups of four. Import the helper after the setup and delegate to it. On a local machine that file would live beside `main.py`.

Edit `main.py`, **Run** to see `3` seals for nine runes, then **Submit**.

## Your Tasks

1. Import `seal_count` from `shrine_rules` after the supplied setup.
2. Complete `prepare_seals(runes)` to return the imported helper’s result.
