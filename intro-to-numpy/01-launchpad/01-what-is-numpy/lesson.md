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

The Pocket Observatory records measurements from small sensors. For one reading, ordinary Python arithmetic is enough. For a whole set of readings, NumPy lets you describe the calculation once and apply it to every value.

NumPy is a Python library. Its main container is an **array**, also called an `ndarray`. An array can hold a line of readings, a grid, or a stack of grids. We'll build those layouts one at a time.

Here are two ways to add a correction of `2` to three readings. Each **Run** block stands alone.

First, a Python list and a loop:

```python run
readings = [3, 5, 7]
corrected = []
for reading in readings:
    corrected.append(reading + 2)
print(corrected)
```

Now, a NumPy array:

```python run
import numpy as np
readings = np.array([3, 5, 7])
print((readings + 2).tolist())
```

Both print `[5, 7, 9]`. The array calculation is **vectorized**: `+ 2` applies to each element, without a loop in your code. `.tolist()` converts the result to a Python list for display so the two outputs are easy to compare.

An array is useful when you have regular numerical data and want to calculate across it. A short list of mixed items may be simpler to keep as a list. NumPy isn't automatically faster for every small job, and converting data takes work too.

Next, we'll look at the import line. Then you'll edit and build arrays yourself.
