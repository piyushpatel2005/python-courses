---
title: "Demo: Format a Message"
slug: format-a-message
order: 3
language: python
lesson_type: coding
summary: Edit one value in a Python f-string and observe the changed message.
seo_title: "Demo: Format a Message | Python Basics"
seo_description: Edit one value in a Python f-string and observe the changed message.
seo_keywords: [python f strings, python format decimals, string interpolation]
---

A bakery displays its daily special. Text can be joined with `+`, but joining numbers that way requires `str(number)`. An **f-string** starts with `f` before the quotes and inserts values at `{name}`. It handles numbers and text in one readable line. In `{price:.2f}`, `.2f` displays a decimal with two places; it does not change the numeric `price`.

The program already works. Change **only** the numeric `price` from `2.5` to `3.75`. Edit `main.py`, press **Run** to see `Bread: $3.75`, then **Submit**. Next, write a label with different data.

## Your Task

1. Set `price` to `3.75` and keep the formatted label.
