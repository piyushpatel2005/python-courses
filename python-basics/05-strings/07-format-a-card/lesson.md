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

Ari copies a cavern waypoint onto a card. An `f` before the quote lets `{name}` insert a value; `{energy:.2f}` shows two decimal places without changing the number. This builds on the f-strings from First Steps.

![f-string parts for the cavern route card](f-string-anatomy.svg "f-string prefix, expression and two-decimal specifier")

Change the f-string in `main.py` so Run prints `GLOW: 7.50 energy`; then Submit. The next sign uses different values.

## Your Task

1. Set `card` with an f-string displaying `energy` to two decimal places.
