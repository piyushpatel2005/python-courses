---
title: "Demo: Convert Text to Numbers"
slug: convert-text-to-numbers
order: 5
language: python
lesson_type: coding
summary: Convert numeric text with int() to calculate a Python quantity.
seo_title: "Demo: Convert Text to Numbers | Python Basics"
seo_description: Convert numeric text with int() to calculate a Python quantity.
seo_keywords: [python type conversion, int from string, numeric strings]
---

Even a response that looks like a number can arrive as text. `"12" + "3"` joins strings into `"123"`; `int("12") + 3` produces `15`. `float("2.5")` reads decimal text. `str(15)` makes text from a number; `int(3.9)` truncates toward zero rather than rounding. Invalid numeric text, such as `"three"`, raises `ValueError`—use known valid values for now.

A market's order count is supplied as a prefilled string. Change **only** `order_text` from `"12"` to `"15"`. Edit `main.py`, press **Run** to see `Items: 17`, then **Submit**. In the next exercise you will convert other strings yourself.

## Your Task

1. Change `order_text` to the string `"15"`; the existing conversion and addition must display 17.
