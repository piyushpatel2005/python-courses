---
title: 'Exercise: Size a shelf'
slug: exercise-math-module
order: 2
language: python
runtime: pyodide
lesson_type: coding
summary: 'Use math.ceil to calculate how many shelf boards to buy.'
seo_title: 'Exercise: Size a shelf | Python Basics'
seo_description: 'Use math.ceil to calculate how many shelf boards to buy.'
seo_keywords: [python math ceil exercise, dimensions, boards]
hints:
  - Divide length by six, then pass the result to math.ceil.
---

A shelf is thirteen metres long, and each board covers six metres. Two boards cover only twelve metres, so you need three. This is the same round-up pattern as the tile calculation, with a different length and board size.

The starter imports `math`. Divide the requested length by six, then use `math.ceil` to round up. For a length of zero, the result is zero.

## Your Task

1. Complete `boards_needed(length)` using `math.ceil` to calculate the number of six-metre boards.

Edit `main.py`. **Run** should print `3` for the supplied length of `13`; **Submit** checks other lengths too.
