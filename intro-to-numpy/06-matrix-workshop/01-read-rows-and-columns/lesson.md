---
title: "Read the grid"
slug: read-rows-and-columns
order: 1
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Read the grid with NumPy arrays."
seo_title: "Read the grid | Intro to NumPy"
seo_description: "Practice read the grid in a runnable NumPy lesson."
seo_keywords: [numpy, arrays, matrices]
hints:
  - Read the shape of the input and the requested result before choosing an axis.
---

An observation grid stores nights in rows and instruments in columns. Indexing `[row, column]` reads one measurement; `grid[:, column]` keeps a whole sensor history. 

Run `main.py` first, make the small edit, then Submit.

## Your Task

1. Change the column index to `1` to show the second sensor’s history `[8 2]`.
