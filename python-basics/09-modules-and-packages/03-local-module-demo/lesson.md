---
title: 'Demo: Import a Local Beacon Rule'
slug: local-module-demo
order: 3
language: python
runtime: pyodide
lesson_type: coding
summary: 'Import a reusable helper from a local Python module.'
seo_title: 'Demo: Import a Local Beacon Rule | Python Basics'
seo_description: 'Import a reusable helper from a local Python module.'
seo_keywords: [python basics, local module demo, python practice]
hints:
  - Change only the argument to the final imported-function call.
---

Ari finds a beacon rule written in another `.py` file. The supplied setup creates `beacon_rules.py` in the browser’s temporary filesystem, then imports `signal_strength`. A regular project would keep that module beside `main.py`; here the single-file runner generates it before the import.

Edit the final call in `main.py` from `2` to `3` marks, **Run** to see `15`, then **Submit**.

## Your Task

1. Change the final `signal_strength` call to use `3` marks.
