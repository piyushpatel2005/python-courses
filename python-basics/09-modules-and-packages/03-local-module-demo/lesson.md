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

You can import your own code too. The supplied setup writes a short file named `beacon_rules.py`, which defines `signal_strength`. The line `from beacon_rules import signal_strength` brings that function into this program, so you can call it by name.

In a local project, you would keep that `.py` file beside `main.py`. This browser example creates the temporary file for you before importing it. Leave that setup in place.

Change only the final call in `main.py` from `2` to `3` marks. Run should show `15`, then Submit.

## Your Task

1. Change the final `signal_strength` call to use `3` marks.
