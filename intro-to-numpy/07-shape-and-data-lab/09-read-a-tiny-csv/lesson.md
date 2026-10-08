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
  - Read the shape of each intermediate array before editing another line.
---

# Read a tiny CSV

An incoming sample arrives as CSV text: each line is a row and each comma separates columns. `np.genfromtxt` reads a file-like object with a delimiter; `StringIO` gives us that object **in memory**. No external URL or persistent browser file is needed. `dtype=int` keeps these whole-number readings numeric; without a deliberate dtype, parsing may produce a different numeric type.

Run the starter first: the mismatched semicolon delimiter treats each comma-separated line as an invalid integer, producing `-1` placeholders instead of two columns. In `main.py`, change **only** `delimiter=";"` to `delimiter=","`. Run again to see the two-column grid, then Submit.

## Your Tasks

1. Use a comma delimiter so `np.genfromtxt` reads the two-column CSV.
