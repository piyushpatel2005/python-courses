---
title: 'Exercise: calibrate rows and reject bad shapes'
slug: exercise-column-broadcast
order: 12
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: A sensor grid receives one baseline per row. The toolkit should also report
  incompatible input without crashing.
seo_title: 'Exercise: calibrate rows and reject bad shapes | NumPy'
seo_description: A sensor grid receives one baseline per row. The toolkit should also
  report incompatible input without crashing. Practice NumPy in the browser.
seo_keywords:
  - NumPy
  - Python
  - column broadcast
hints:
  - A `(rows, 1)` column expands across columns; wrap only the attempted operation in
    `try`.
---

A sensor grid receives one baseline per row. The toolkit should also report incompatible input without crashing.

Use the preceding editable example as a pattern, but solve this new data task in `main.py`.

## Your Tasks

1. Use `[:, np.newaxis]` to subtract one entry of `baselines` from every column in its matching row.
2. In `incompatible`, try `grid + offsets`; return `True` on `ValueError` and `False` when it succeeds.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check each task.
