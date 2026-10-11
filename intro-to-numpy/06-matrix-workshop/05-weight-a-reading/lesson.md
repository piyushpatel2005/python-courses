---
title: "Weight a reading"
slug: weight-a-reading
order: 5
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: 'Combine paired readings and weights into one total with np.dot.'
seo_title: "Weight a reading | Intro to NumPy"
seo_description: 'Combine paired readings and weights into one total with np.dot.'
seo_keywords: [numpy, arrays, matrices]
hints:
  - Replace the whole expression readings * weights with a call to np.dot.
---

Some instruments contribute more to a combined reading than others. A weight tells us how much each reading contributes. A 1D dot product multiplies corresponding readings and weights, then adds those products into one number. The two input arrays must have the same length.

For the starter data, `2×3 + 4×1 + 6×2` gives `22`. By comparison, `readings * weights` stops at the separate products `[6 4 12]`. Use `np.dot(readings, weights)` when you want their combined total.

Run the starter to see those separate products. Edit `main.py`, Run again to see one number, then Submit.

## Your Task

1. Set `weighted` to `np.dot(readings, weights)` to compute the single weighted total.
