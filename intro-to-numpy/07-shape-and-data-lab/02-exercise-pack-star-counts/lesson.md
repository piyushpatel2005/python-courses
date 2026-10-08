---
title: 'Exercise: pack star counts'
slug: exercise-pack-star-counts
order: 2
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Unroll a count grid and repack arbitrary groups of four.
seo_title: 'Exercise: pack star counts | Intro to NumPy'
seo_description: Unroll a count grid and repack arbitrary groups of four.
seo_keywords:
  - numpy
  - array shape
  - exercise pack star counts
hints:
  - Read the shape of each intermediate array before editing another line.
---

# Exercise: pack star counts

A different station sends star counts as rows. Transfer the shape pattern from the signal card: `ravel()` makes a one-dimensional reading order, and `reshape(-1, 4)` infers the number of rows while keeping four columns. The number of values still must be divisible by four.

Edit `main.py`, press Run to see the flat and packed readings, then Submit. The tests also call your functions with different-sized inputs.

## Your Tasks

1. Return a row-major flat array from `unroll_counts(grid)` using `ravel()`.
2. Return four-column rows from `pack_counts(readings)` using `reshape(-1, 4)`.
