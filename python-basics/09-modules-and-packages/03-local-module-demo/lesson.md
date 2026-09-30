---
title: "Local Module: Demo"
slug: local-module-demo
order: 3
language: python
runtime: pyodide
lesson_type: coding
summary: Import a small module generated in the browser filesystem.
seo_title: "Local Module: Demo | Python Basics"
seo_description: Import a small module generated in the browser filesystem.
seo_keywords: [python basics, local module demo, python practice]
hints:
  - Change only the argument to the final imported-function call.
---

# Local Module: Demo

Your own `.py` file can also be a module. This lesson keeps one editable `main.py` tab: its supplied setup writes `route_rules.py` into the browser's temporary in-memory filesystem, then imports its `travel_minutes` function. The file is not saved to your computer and will not survive a fresh session. On your machine you would keep `route_rules.py` beside `main.py`; the current lesson runner submits one active Python file, so the setup creates that local module before importing it. Change the call from 2 to 3 stops; Run and compare the result.

## Your Tasks

1. Change the argument in the final `travel_minutes` call to `3` so it prints `15`.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your change.
