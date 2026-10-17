---
title: "Put Values in an f-String"
slug: f-string-messages
order: 7
language: python
lesson_type: coding
summary: "Use an f-string to put live variables into a printed message."
seo_title: "Print Variables with Python f-Strings | Python Basics"
seo_description: "Build readable output with Python f-strings and braces around variable names."
seo_keywords: [python basics, f-string, string interpolation, print strings]
---

You now know how to join strings with `+`, fill percent placeholders, and use `.format()` method on string data. An **f-string** is a more convenient way to put variables into a message.

## Place variables between braces

Write `f` immediately before the opening quote. Put a variable name inside `{}` where its value should appear:

```python run
keeper = "Mira"
visits = 2
print(f"{keeper} checked the gate {visits} times")
```

This prints `Mira checked the gate 2 times`. The braces are instructions in the code, not part of the output. You do not need `str(visits)` here as f-string handles the integer. If you leave off the `f`, Python prints the braces and names literally without replacing them with values.

## Your Tasks

In `main.py`, replace `"TODO"` with an f-string using the supplied `pathfinder` and `coins`. Leave the print call in place.

1. Set `status_line` so it prints `Adam found 3 coins`.

Press **Run** to inspect the line, then **Submit**. The following lesson builds on this idea to display a decimal value with two places.
