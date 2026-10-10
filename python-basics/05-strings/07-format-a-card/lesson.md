---
title: "Format a Route Card: Demo"
slug: format-a-card
order: 7
language: python
lesson_type: coding
runtime: pyodide
summary: Format a decoded route card with an f-string.
seo_title: "Format a Route Card: Demo | Python Basics"
seo_description: Format a decoded route card with an f-string.
seo_keywords: [python basics, strings, lantern atlas]
---

# Format a Route Card: Demo

The route card already contains a name and an energy amount. Give the amount a consistent format so `7.5` appears as `7.50`.

An **f-string** has an `f` before its opening quote. Expressions inside braces supply the values: `{name}` inserts the name, and `{energy:.2f}` displays the energy with two digits after the decimal point.

![An f-string inserts the route name and formats energy with two decimal places](f-string-anatomy.svg "f-string prefix, expression and two-decimal specifier")

The formatting changes the text on the card, not the number stored in `energy`.

## Your Task

1. Update the f-string assigned to `card` so it displays `energy` to two decimal places.

Keep the name and the word `energy` in the card. Run `main.py` to see `GLOW: 7.50 energy`, then Submit.
