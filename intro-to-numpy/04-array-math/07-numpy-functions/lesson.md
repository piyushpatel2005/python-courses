---
title: Apply functions to a full array
slug: numpy-functions
order: 7
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: Apply NumPy sine, cosine, logarithm, and exponential functions to whole arrays.
seo_title: Apply functions to a full array | NumPy
seo_description: Transform whole arrays with NumPy sine, cosine, logarithm, and exponential functions.
seo_keywords:
  - NumPy
  - Python
  - numpy functions
hints:
  - Use NumPy functions directly on whole arrays; angles are in radians.
---

An angle sensor can transform several angles at once.

`np.sin` and `np.cos` use radians. `np.log` needs positive inputs for finite real results; `np.exp` reverses log on modest values. Each function acts on every array element.

## Your Task

1. Change `np.cos` to `np.sin` and Run. The log examples deliberately avoid zero.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check the change.
