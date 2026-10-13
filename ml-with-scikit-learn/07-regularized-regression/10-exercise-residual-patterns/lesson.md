---
title: 'Exercise: inspect residual patterns'
slug: exercise-residual-patterns
order: 10
language: python
lesson_type: coding
runtime: pyodide
summary: Plot validation residuals against predictions and report a visible limitation
  without inferring causality.
seo_title: 'Exercise: inspect residual patterns | Scikit-Learn'
seo_description: Plot validation residuals against predictions and report a visible
  limitation without inferring causality with a different practice fixture.
seo_keywords:
  - scikit-learn
  - residual patterns
  - Python
pyodide_packages:
  - numpy
  - scikit-learn
  - matplotlib
---

The cabinet-price fixture has six predictions and a wider curved pattern. The supplied interpretation is already tied to this fixture; implement the chart from arguments so a changed fixture still plots the right paired values.

Your helper returns the figure and axes so the supplied probe can label and display the result. Use one scatter collection and `ax.axhline(0, ...)` for a reference. The task fixes the residual direction; chart styling and a short interpretation are supplied rather than added as independent requirements. Do not use the sealed test plot to repeatedly redesign the model.

## Your Tasks

1. Implement `residual_plot(actual, predicted)` to return `(fig, ax)` with a scatter of predictions against observed-minus-predicted residuals and a horizontal zero reference. Label both axes in dollars.

Edit `main.py`, press **Run** to inspect the supplied output, then **Submit** to check this task.
