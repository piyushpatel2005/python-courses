---
title: "Demo: Format a Gear Label"
slug: format-a-message
order: 3
language: python
lesson_type: coding
summary: "Use a two-decimal f-string to display a gear cost."
seo_title: "Demo: Format a Gear Label | Python Basics"
seo_description: "Use a two-decimal f-string to display a gear cost."
seo_keywords: [python basics, values and input, lantern atlas]
---

A gear label needs text and a price on the same line. An **f-string** lets you put values into text without printing them separately.

In **main.py**, notice the `f` before the opening quote. Each pair of braces marks a value to insert: `{gear}` inserts the item name, while `{cost:.2f}` inserts the cost with two digits after the decimal point. The `$` is ordinary text.

Run the starter to see `Compass: $2.50`. Formatting adds the displayed zero; it does not change the number stored in `cost`.

You could also join strings with `+`, but a number would first need conversion with `str(number)`. An f-string handles that display work for you. Conversion gets its own lesson shortly.

Keep the print call and change the cost assignment in **main.py**. Press **Run** to see `Compass: $3.75`, then **Submit**.

## Your Tasks

1. Set `cost` to `3.75`.
