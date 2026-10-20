---
title: "Exercise: Slice a Stock Label"
slug: exercise-slice-ticket
order: 4
language: python
runtime: pyodide
lesson_type: coding
summary: Slice a stock label into its category and item code.
seo_title: "Exercise: Slice a Stock Label | Python Basics"
seo_description: Slice a stock label into its category and item code.
seo_keywords: [python basics, strings, python strings, slicing, stock code]
---

# Exercise: slice a stock label

A stock label reads `BOX:2048`. The first three letters describe the category and the four digits after the colon identify the item. The colon is at index `3`.

Keep `record` unchanged and use slices to read the two fields. Leave the item code as text: you are identifying an item, not doing arithmetic with its number.

## Your Tasks

1. Set `category` to a slice containing the first three characters of `record`.
2. Set `item_code` to a slice containing the four digits after the colon.

After the first task, Run shows `BOX None`. After both, it shows `BOX 2048`. Submit to check the slices with another record.
