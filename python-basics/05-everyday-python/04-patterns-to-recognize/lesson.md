---
title: Patterns to Recognize
slug: patterns-to-recognize
order: 4
language: python
lesson_type: informational
runtime: pyodide
summary: Recognize recursion’s base case and fixed named choices in a beacon mission.
seo_title: Recursion and Enums at a Glance | Python Basics
seo_description: Introduce recursive base cases and enum choices without requiring either in Ari’s final mission.
seo_keywords: [python recursion, base case, python enum, beginner concepts]
---

# Patterns to recognize

A beacon sequence can repeat in smaller steps. **Recursion** means a function calls itself on a smaller problem. A *base case* stops the calls; without one, Python eventually raises `RecursionError`. This read-only example counts down:

```python
def count_down(number):
    if number == 0:  # Base case: stop here.
        return "Beacon ready"
    return count_down(number - 1)  # Move toward zero.
```

For the small lists in Ari’s mission, a `for` loop is simpler. You will not need recursion in the final project.

An **enum** groups a fixed set of named choices. A beacon could have states named `DARK`, `LIT`, and `RESTORED` instead of arbitrary status strings. Python's `enum` module provides this pattern, but writing an enum uses class syntax, which is beyond this project. Keep using strings and conditionals for the final beacon report.
