---
title: "Exercise: Format an Invoice"
slug: exercise-format-an-invoice
order: 4
language: python
lesson_type: coding
summary: Use f-strings to produce a readable invoice line and formatted total.
seo_title: "Exercise: Format an Invoice | Python Basics"
seo_description: Use f-strings to produce a readable invoice line and formatted total.
seo_keywords: [python f string exercise, format currency, invoice strings]
---

A print shop needs a compact invoice for posters. The starter already calculates `total`; change only the placeholder message assignments. Prefix each string with `f` so braces insert live variable values. Use `{total:.2f}` to show two decimal places in the price. The supplied print calls display your messages.

Edit `main.py`, press **Run** to inspect the two invoice lines, then **Submit**.

## Your Tasks

1. Set `heading` with an f-string to `4 posters for the art fair`, using `quantity` and `event`.
2. Set `payment_line` with an f-string to `Due: $10.00`, using `total` formatted to two decimal places.
