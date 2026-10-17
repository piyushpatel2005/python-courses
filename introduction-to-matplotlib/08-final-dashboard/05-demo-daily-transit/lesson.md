---
title: 'Demo: Sum daily transit rides'
slug: demo-daily-transit
order: 5
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - matplotlib
  - numpy
  - pandas
summary: 'Group routes into daily ride totals for a line chart.'
seo_title: 'Demo: Sum daily transit rides | Introduction to Matplotlib'
seo_description: 'Group routes into daily ride totals for a line chart.'
seo_keywords:
  - 'matplotlib'
  - 'python visualization'
  - 'neighborhood signals'
  - 'demo'
  - 'sum'
  - 'daily'
hints:
  - 'Check the Axes labels, data and limits before changing the style.'
---

# Demo: Sum daily transit rides

On one day, several routes carry passengers. The day total is a **sum**, not a mean of route counts. This demo groups those rows and draws a line. Change the marker so actual observation days stand out; connecting segments only guide the eye between recorded dates.

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. Use marker `o` for the daily total line.
