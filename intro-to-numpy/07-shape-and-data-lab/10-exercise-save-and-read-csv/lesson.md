---
title: 'Exercise: save and read CSV'
slug: exercise-save-and-read-csv
order: 10
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Round-trip a numeric grid through a tiny in-memory CSV.
seo_title: 'Exercise: save and read CSV | Intro to NumPy'
seo_description: Round-trip a numeric grid through a tiny in-memory CSV.
seo_keywords:
  - numpy
  - array shape
  - exercise save and read csv
hints:
  - Read the shape of each intermediate array before editing another line.
---

# Exercise: save and read CSV

The weather sensor has a different grid. `np.savetxt` writes rows to a file-like object, and `np.genfromtxt` reads them back. Use `StringIO` for both directions: create the buffer, write into it, then read from fresh `StringIO(text)` (or rewind it with `seek(0)`). The result is plain CSV text, not a download saved outside this lesson.

Edit `main.py`, Run to inspect the text and recovered rows, then Submit. Keep `fmt="%d"` so the sample uses whole numbers.

## Your Tasks

1. Return comma-separated, newline-terminated whole-number CSV text from `save_grid(grid)` using `np.savetxt` and `StringIO`.
2. Return a two-dimensional integer array from `read_grid(text)` using `np.genfromtxt` and `StringIO` (including one-row inputs).
