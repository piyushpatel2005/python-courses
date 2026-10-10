---
title: 'Exercise: Label any observation'
slug: exercise-inspect-array-metadata
order: 10
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Report ndim, shape, size, and first-axis length for observation arrays.
seo_title: 'Exercise: Label any observation | NumPy for beginners'
seo_description: Report ndim, shape, size, and first-axis length for observation arrays.
seo_keywords:
  - NumPy
  - Python arrays
  - exercise inspect array metadata
---

Write a label for an observation without assuming its layout. The input is already a NumPy array, so you don't need to convert it again.

Return one tuple containing these four pieces of information, in order:

- the number of axes;
- the shape tuple;
- the total number of elements;
- the length of the first axis.

Use the attributes from the previous lesson. `len(observation)` is a function call; the attributes don't need parentheses. The inputs here are arrays with at least one axis, not scalar arrays.

## Your Tasks

1. Complete `describe_observation(observation)` so it returns the four-part tuple described above.

Run `main.py` to inspect `(2, (2, 3), 6, 2)` for the sample grid, then Submit to check other layouts.

You can now create an array and describe its structure. After the quiz, you'll generate regular sequences and starter grids without typing every value by hand.
