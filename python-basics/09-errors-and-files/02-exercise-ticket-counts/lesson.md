---
title: 'Exercise: Label a receipt quantity'
slug: exercise-ticket-counts
order: 2
language: python
lesson_type: coding
runtime: pyodide
summary: 'Convert quantity text safely and make a receipt label.'
seo_title: 'Exercise: Label a receipt quantity | Python Basics'
seo_description: 'Convert quantity text safely and make a receipt label.'
seo_keywords: [python try except exercise, ValueError, receipt quantity]
---

A receipt label should show `0` rather than crash if a quantity field contains invalid text. Write a conversion helper first, then use it to build a label. For example, `quantity_label("2")` should return `"Quantity: 2"`.

Use `try` and `except ValueError` around `int(text)`. Catching this specific error keeps unrelated mistakes visible. The second helper should call the first; that way both valid and invalid values follow the same rule.

## Your Tasks

1. Complete `quantity_value(text)` to return `int(text)` or `0` when conversion raises `ValueError`.
2. Complete `quantity_label(text)` to return `"Quantity: <count>"` using `quantity_value(text)`.

Edit `main.py`, press **Run** to inspect the two example labels, then **Submit**. You can submit after each task; the tests check the helpers separately.
