---
title: 'Exercise: calibrate rows and reject bad shapes'
slug: exercise-column-broadcast
order: 12
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: "Correct each grid row and detect incompatible broadcasting shapes."
seo_title: 'Exercise: calibrate rows and reject bad shapes | NumPy'
seo_description: "Correct each grid row and detect incompatible broadcasting shapes."
seo_keywords:
  - NumPy
  - Python
  - column broadcast
hints:
  - 'Keep the correction and the error check separate; only the correction adds an axis.'
---

The observatory toolkit now needs one correction per row and a small check for incompatible inputs. These are separate functions: the shape check tests the arrays it receives without reshaping them.

Use `baselines[:, np.newaxis]` for the correction. In the compatibility check, put only `grid + offsets` inside `try`; catch `ValueError`, then return `False` after the `except` block when addition succeeds.

## Your Tasks

1. In `row_correction`, subtract `baselines[:, np.newaxis]` from `grid`.
2. In `incompatible`, return `True` if `grid + offsets` raises `ValueError`, or `False` if it succeeds.

Run `main.py` after each edit, then Submit. You can now calibrate whole grids; the next section turns those grids into totals and statistics.
