---
title: 'Import a local shipping helper'
slug: local-module-demo
order: 3
language: python
runtime: pyodide
lesson_type: coding
summary: 'Call a shipping helper imported from a local module.'
seo_title: 'Import a local shipping helper | Python Basics'
seo_description: 'Call a shipping helper imported from a local module.'
seo_keywords: [python local module, from import, shipping helper]
hints:
  - Change the argument to the final imported-function call.
---

You can import code from your own files. The supplied setup writes a small `shipping_rules.py` file with a `shipping_cost(weight)` function. It charges five dollars per kilogram. The line `from shipping_rules import shipping_cost` brings the function into `main.py` so you can call it directly.

In a local project, you would keep `shipping_rules.py` beside `main.py`. This browser exercise creates the file in its temporary Python environment before the import, because the editor only exposes `main.py`. Leave that setup in place; it is not a permanent file on your device.

## Your Task

1. Change the final `shipping_cost` call from `2` to `3` kilograms.

Edit `main.py`, then **Run** to see the cost change from `10` to `15`. Press **Submit** to check it.
