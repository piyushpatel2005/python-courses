---
title: Render the complete invoice
slug: invoice-total
order: 11
language: python
lesson_type: coding
summary: Add an order heading and total around the formatted invoice lines.
seo_title: Render the complete invoice | Python OOP practice
seo_description: Add an order heading and total around the formatted invoice lines.
seo_keywords:
  - Python
  - invoice total
  - object oriented programming
hints:
  - Start with the heading, extend with lines(), then append the total.
---

# Render the complete invoice

Add an order heading and total around the formatted invoice lines.

The invoice renderer composes earlier behavior rather than recalculating a purchase from a current catalog. A list of text lines is convenient while building the document; `"\n".join(parts)` turns it into one printable string. Use the stored total. The result has no trailing newline, leaving the final print operation responsible for ending the Console line.

An empty invoice still needs its heading and a zero total, with no blank item line between them. Build the complete list of lines first, then join once. Do not print inside render; returning text lets the command layer decide when to display it.

## A smaller example

The travel log joins a list into one multiline string.

```python
parts = ["Travel log", "Ridge trail", "Distance: 850 m"]
print("\n".join(parts))
```

## Your Tasks

1. Implement `Invoice.render()` to join `"Order ID"`, all values from `lines()`, and `"Total: $D.CC"` with newlines. Substitute the actual ID and stored total, with no trailing newline.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. The finished invoice has an order heading, a Mug line, and `Total: $25.00`. Press **Submit** to check the behavior with other inputs.
