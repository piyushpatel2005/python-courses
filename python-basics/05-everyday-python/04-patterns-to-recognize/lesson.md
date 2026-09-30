---
title: Patterns to Recognize
slug: patterns-to-recognize
order: 4
language: python
lesson_type: informational
runtime: pyodide
summary: Recognize recursion's base case and the idea of a fixed set of enum values.
seo_title: Recursion and Enums at a Glance | Python Basics
seo_description: A beginner overview of recursive base cases and named enum values without adding either to the final workshop project.
seo_keywords: [python recursion, base case, python enum, beginner concepts]
---

Workshop tasks sometimes repeat in smaller pieces. **Recursion** is when a function calls itself on a smaller problem. It needs a *base case* that stops the calls; otherwise Python eventually raises `RecursionError`. This read-only example counts down:

```python
def count_down(number):
    if number == 0:  # Base case: stop here.
        return "Done"
    return count_down(number - 1)  # Move toward zero.
```

For the small lists in this course, a `for` loop is usually simpler. You will not need recursion in the project.

An **enum** groups a fixed set of named choices. A workshop might use statuses named `OPEN`, `FULL`, and `CANCELLED` rather than a collection of arbitrary status strings. Python's `enum` module provides this pattern, but writing an enum requires class syntax, which is beyond this beginner project. Keep using familiar strings and conditionals for the final report; there is no enum-writing task here.
