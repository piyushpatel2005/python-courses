---
title: Patterns to Recognize
slug: patterns-to-recognize
order: 4
language: python
lesson_type: informational
runtime: pyodide
summary: Recognize recursion’s base case and fixed named choices in a beacon mission.
seo_title: Recursion and Enums at a Glance | Python Basics
seo_description: Introduce recursive base cases and enum choices without requiring either in Adi’s final mission.
seo_keywords: [python recursion, base case, python enum, beginner concepts]
---

# Patterns to recognize

Some Python programs use a function that calls itself. This is called **recursion**. A beacon countdown gives us a small example to read:

```python
def count_down(number):
    if number == 0:  # Base case: stop here.
        return "Beacon ready"
    return count_down(number - 1)  # Move toward zero.
```

Imagine calling `count_down(2)`. That call asks `count_down(1)` for its result, which asks `count_down(0)`. At zero, the function returns `"Beacon ready"` rather than calling itself again. That result then returns through the waiting calls.

The stopping condition is the **base case**. Each call needs to move toward it. This example expects a non-negative integer: starting with a negative number would keep moving away from zero until Python raises `RecursionError`.

For the small lists in Adi's final mission, use a `for` loop. You don't need recursion to write the report.

## Named choices with enums

A beacon might be `DARK`, `LIT`, or `RESTORED`. An **enum** groups choices like these under one name, so code can refer to a defined member rather than repeatedly typing a status string.

Python provides enums in the `enum` module. Defining one with class syntax is a topic for later; for this mission, strings and conditionals are enough. For now, recognize an enum as a way to name a fixed set of choices.
