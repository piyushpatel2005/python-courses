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

A shrine rule already knows how many seals a group of runes needs. Reuse it rather than writing that calculation again.

The supplied setup creates the temporary `shrine_rules.py` file and its `seal_count` function. Import the function after that setup, then call it from `prepare_seals`. In a local project, the module file would sit beside `main.py`.

Edit `main.py`, Run to check that nine runes need `3` seals, then Submit.

## Your Tasks

1. Import `seal_count` from `shrine_rules` after the supplied setup.
2. Complete `prepare_seals(runes)` to return the imported helper’s result.
