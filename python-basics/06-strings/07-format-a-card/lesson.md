---
title: "Format a Price Tag: Demo"
slug: format-a-card
order: 7
language: python
runtime: pyodide
lesson_type: coding
summary: Use an f-string to display a price with two decimal places.
seo_title: "Format a Price Tag: Demo | Python Basics"
seo_description: Use an f-string to display a price with two decimal places.
seo_keywords: [python basics, strings, python f-strings, decimal formatting, prices]
---

# Format a price tag

A price tag has a product name and a dollar amount. Display `7.5` as `$7.50` so the amount reads like a price.

An **f-string** starts with `f` before the quote. Braces insert values: `{name}` inserts the product name, and `{price:.2f}` displays the price with two digits after the decimal point.

![An f-string inserts a product name and formats its price to two decimal places](f-string-anatomy.svg "f-string prefix, expression and price format")

The formatting changes the displayed text, not the number stored in `price`.

## Your Task

1. Update the f-string assigned to `card` so it displays `price` to two decimal places.

Keep the name and the dollar sign. Run `main.py` to see `Notebook: $7.50`, then Submit.
