---
title: "Loop through a price list"
slug: loop-through-prices
order: 3
language: python
lesson_type: coding
runtime: pyodide
summary: "Read dictionary keys and values together with items()."
seo_title: "Loop through a price list | Python Basics"
seo_description: "Read dictionary keys and values together with items()."
seo_keywords: [python basics, python collections, beginner python]
---

A small price list maps product names to dollar amounts. Calling `prices.items()` gives you key-value pairs. The loop `for product, price in prices.items():` unpacks each pair into two names, just as you unpacked a tuple. Use `.keys()` when you only need product names, or `.values()` when you only need prices.

The starter collects the prices, but you need the product names. Change the append call in `main.py`. **Run** should print `['apple', 'banana']`; then **Submit**.

## Your Task

1. Loop through `prices.items()` and append each product name to `products`.
