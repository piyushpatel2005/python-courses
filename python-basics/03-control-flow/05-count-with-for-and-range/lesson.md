---
title: Count with for and range
slug: count-with-for-and-range
order: 5
language: python
runtime: pyodide
lesson_type: coding
summary: Use a for loop to iterate the values from range.
seo_title: Count with for and range | Python Basics
seo_description: Use a for loop to iterate the values from range. Practice Python
  control flow in an editable browser lesson.
seo_keywords:
- python for loop
- range start stop step
- python iteration
---

# Count with for and range

A market prints stall labels. `for stall in range(1, 4)` visits 1, 2, and 3: the stop value 4 is excluded. `range(4)` starts at 0; `range(2, 8, 2)` visits 2, 4, and 6 because the third argument is the step. Unlike a `while` loop, a `for` loop automatically moves to the next value.

The starter prints `Stall 1 | Stall 2 | Stall 3 | `. Edit **main.py** and change `range(1, 4)` to `range(1, 5)`. Press **Run** to see `Stall 4 | ` added at the end; press **Submit** to check your edit.

## Your Task

1. Change the range endpoint to `5` so the program includes stall 4.
