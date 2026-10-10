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
  - Write with np.savetxt(buffer, grid, delimiter=",", fmt="%d"); read with ndmin=2.
---

# Exercise: save and read CSV

The weather sensor needs to send a grid as text and recover it later. Write two helpers so you can check each direction on its own.

`StringIO()` creates an empty text buffer. `np.savetxt(buffer, values, delimiter=",", fmt="%d")` writes numeric rows into it. Here, `fmt="%d"` writes whole numbers, and `buffer.getvalue()` returns the finished string, including a newline after each row.

For example, this separate one-row grid becomes the text `'8,1\n'`:

```python
from io import StringIO
import numpy as np

buffer = StringIO()
np.savetxt(buffer, np.array([[8, 1]]), delimiter=",", fmt="%d")
text = buffer.getvalue()
print(repr(text))
print(np.genfromtxt(StringIO(text), delimiter=",", dtype=int, ndmin=2))
```

When reading, `ndmin=2` keeps at least two dimensions. Without it, a one-row CSV usually becomes a one-dimensional array rather than a grid. A fresh `StringIO(text)` starts reading at the beginning; if you reuse the written buffer instead, rewind it with `buffer.seek(0)` first.

The buffer is temporary practice data created by your code, not a downloaded or saved file. Edit `main.py`, Run after each helper, then Submit. The supplied `repr(text)` print makes newline characters visible.

## Your Tasks

1. Implement `save_grid(grid)` with `np.savetxt` and `StringIO` to return comma-separated integer CSV text ending in a newline.
2. Implement `read_grid(text)` with `np.genfromtxt` and `StringIO` to return a two-dimensional integer array, including for one-row inputs.
