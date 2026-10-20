---
title: "Exercise: Label today's orders"
slug: exercise-pack-deliveries
order: 6
language: python
lesson_type: coding
runtime: pyodide
summary: "Slice the first three orders and create a label for each."
seo_title: "Exercise: Label today's orders | Python Basics"
seo_description: "Slice the first three orders and create a label for each."
seo_keywords: [python basics, python collections, beginner python]
---

A packing table has four order IDs, but only the first three are due today. Use a slice to choose those IDs. Then loop over that selection and add a label for each order. For example, a label for `order 205` would be `Pack order 205`.

The starter supplies the order list, an empty `labels` list, and a print statement. Edit `main.py`, press **Run** to inspect both lists, then **Submit**.

## Your Tasks

1. Set `today` to a slice of the first three `orders`.
2. Loop over the first three orders and append `Pack <order ID>` strings to `labels`.
