---
title: "Project: Print a Simple Receipt"
slug: project-workshop-receipts
order: 9
language: python
runtime: pyodide
lesson_type: coding
summary: Calculate an item total and return a reusable receipt line.
seo_title: "Project: Print a Simple Receipt | Python Basics"
seo_description: Calculate an item total and return a reusable receipt line.
seo_keywords: [python basics, functions and reuse, python functions, receipt, return values]
hints:
  - Return from each function; the supplied print calls display both results.
---

# Project: print a simple receipt

A stationery counter needs a total and a short receipt line for each purchase. One function multiplies quantity by unit price; another labels the resulting dollar amount. Use the parameters so the same functions work for other items.

## Your Tasks

1. Complete `receipt_total(quantity, price)` so it returns `quantity * price` (a total in dollars).
2. Complete `receipt_line(item, amount)` so it returns `item: $amount` using its parameters.

Work in `main.py`; the print calls are supplied. After the first task, Run shows `Total: $12` even while the line function is unfinished. After the second, it also shows `Notebooks: $12`.

Submit to check both functions with other purchases. Next, you'll read parts of ordinary text such as room labels and stock codes.
