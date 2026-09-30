---
title: "Demo: Inspect Data Types"
slug: inspect-data-types
order: 6
language: python
lesson_type: coding
summary: Use type() to inspect Python text, integers, and decimals.
seo_title: "Demo: Inspect Data Types | Python Basics"
seo_description: Use type() to inspect Python text, integers, and decimals.
seo_keywords: [python data types, python type function, int float str]
---

A sign can have text and numbers. `"Tea"` is a string (`str`); `8` is an integer (`int`); `2.5` is a decimal (`float`). Python determines their types from the values, without declarations. `type(value).__name__` displays the short type name instead of Python's longer `<class 'str'>` form.

The working program describes a café item. Edit **only** `price` from `2.5` to `3.5` in `main.py`. Press **Run**: the price changes, while its type still displays `float`. Press **Submit**. Booleans (`True`/`False`), collections, and `None` exist too; later sections give them their own uses.

## Your Task

1. Set `price` to the decimal `3.5`.
