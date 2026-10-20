---
title: 'Exercise: Import a tax helper'
slug: exercise-local-module
order: 4
language: python
runtime: pyodide
lesson_type: coding
summary: 'Import a local tax calculation and reuse it in a function.'
seo_title: 'Exercise: Import a tax helper | Python Basics'
seo_description: 'Import a local tax calculation and reuse it in a function.'
seo_keywords: [python local module exercise, from import, tax helper]
hints:
  - Use from tax_rules import sales_tax, then call sales_tax(subtotal).
---

A small checkout program needs a tax calculation. The supplied setup creates a temporary `tax_rules.py` file with `sales_tax(subtotal)`, which returns ten percent of a dollar subtotal. Instead of copying that calculation into `main.py`, import and call the helper.

The setup must run before the import. In an ordinary local project, you would save `tax_rules.py` beside `main.py`; here the browser example creates it for this run. A subtotal of `40` gives `4.0` dollars of tax.

## Your Tasks

1. Import `sales_tax` from `tax_rules` after the supplied setup.
2. Complete `tax_for_order(subtotal)` to return the result of calling the imported `sales_tax(subtotal)` helper.

Edit `main.py`. **Run** should print `4.0`; **Submit** checks the import and the function separately.
