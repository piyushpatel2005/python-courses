---
title: Stamp a pattern
slug: stamp-a-pattern
order: 7
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Distinguish element repeats from whole-pattern tiling.
seo_title: Stamp a pattern | Intro to NumPy
seo_description: Distinguish element repeats from whole-pattern tiling.
seo_keywords:
  - numpy
  - array shape
  - stamp a pattern
hints:
  - The repeat count controls adjacent copies of each value, not copies of the whole sequence.
---

# Stamp a pattern

An exposure schedule can hold a setting for several frames or cycle through a set of settings. Those are different orders, even when they use the same values.

`np.repeat([2, 5], 2)` gives `[2, 2, 5, 5]`: it repeats each value beside itself. `np.tile([2, 5], 2)` gives `[2, 5, 2, 5]`: it copies the whole pattern. Unlike `np.newaxis`, these operations increase the number of values when the repeat count is greater than one.

The same idea works on a column. In `np.repeat(column, 2, axis=0)`, `axis=0` selects whole rows to repeat. Without an axis, `repeat` flattens its input first. For tiling a 2D array, a pair such as `(1, 2)` means one copy in the row direction and two copies in the column direction:

```python
import numpy as np

column = np.array([[3], [8]])
held = np.repeat(column, 2, axis=0)
paired = np.tile(held, (1, 2))
print(paired)
# [[3 3]
#  [3 3]
#  [8 8]
#  [8 8]]
```

For now, keep the editable example one-dimensional. In `main.py`, change the repeat count from `2` to `3`, then Run. Compare the three adjacent copies of each value with the unchanged cycling pattern. Submit to check `held`.

## Your Tasks

1. Use `np.repeat` to repeat each exposure value three times in `held`.
