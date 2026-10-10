---
title: Read a tiny CSV
slug: read-a-tiny-csv
order: 9
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Load comma-separated sensor numbers from an in-memory file.
seo_title: Read a tiny CSV | Intro to NumPy
seo_description: Load comma-separated sensor numbers from an in-memory file.
seo_keywords:
  - numpy
  - array shape
  - read a tiny csv
hints:
  - Match delimiter to the commas in csv_text; keep dtype=int for these whole numbers.
---

# Read a tiny CSV

A small sensor packet arrives as CSV text. Each line is a row, and each comma separates two readings. `np.genfromtxt` can read this text through a file-like object. `StringIO(csv_text)` supplies that object in memory, so you do not need a file on disk or an external URL.

The `delimiter` argument tells NumPy where one field ends and the next begins. `dtype=int` asks for whole-number readings; the default would be floating point. These examples contain only numeric rows, with no header or missing fields.

Run `main.py` before editing it. The incorrect semicolon delimiter makes each comma-separated line an invalid integer field, so the starter shows `-1` placeholders instead of two columns. Change the delimiter, Run again, and compare the shape and values. Submit when you can see the two-by-two grid.

## Your Tasks

1. Set the `np.genfromtxt` delimiter to a comma so `readings` contains the two-column CSV data.
