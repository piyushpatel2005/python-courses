---
title: What is NumPy?
slug: what-is-numpy
order: 1
language: python
lesson_type: interactive
runtime: pyodide
pyodide_packages:
  - numpy
summary: Compare a small Python list with vectorized NumPy arithmetic and choose the
  right tool.
seo_title: What is NumPy? | NumPy for beginners
seo_description: Compare a small Python list with vectorized NumPy arithmetic and
  choose the right tool.
seo_keywords:
  - NumPy
  - Python arrays
  - what is numpy
---


The Pocket Observatory receives repeated sensor readings. NumPy stores a grid of values in an `ndarray`, so you can express the same operation across all readings without writing a Python loop. It is useful for large, consistently typed numeric data; a short mixed list or a one-off tally may be simpler as a Python list. NumPy is not automatically faster for every tiny job, and converting data has a cost.

Each **Run** block stands alone. Run both and compare the output:

```python run
readings = [3, 5, 7]
print([reading + 2 for reading in readings])
```

```python run
import numpy as np
readings = np.array([3, 5, 7])
print((readings + 2).tolist())
```

Both produce the same values. The second addition is **vectorized**: NumPy applies it element by element. `.tolist()` only makes the printed form easy to compare; the arithmetic happened on an array. You will build one yourself next.
