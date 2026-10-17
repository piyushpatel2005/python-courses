---
title: "Exercise: Format Forge Readouts"
slug: exercise-format-an-invoice
order: 9
language: python
lesson_type: coding
summary: "Build two f-string HUD lines from live gear values."
seo_title: "Exercise: Format Forge Readouts | Python Basics"
seo_description: "Build two f-string HUD lines from live gear values."
seo_keywords: [python basics, values and input, lantern atlas]
---

In this lesson, you'll build two readouts for a flare purchase. One says what you are buying, and the other shows its cost.

The starter already calculates `cost` from the flare count and price. Its print calls are ready too. Replace the two `"TODO"` strings in **main.py** with f-strings using the supplied variables. Remember that `:.2f` belongs inside the braces, after the numeric variable name.

## Your Tasks

1. Set `gear_line` to an f-string using `flare_count` and `forge` that displays `4 flares for Gear Forge`.
2. Set `cost_line` to an f-string using `cost` that displays `Cost: $10.00`, with two decimal places.

Press **Run** to read both lines. The cost should show two decimal places even though it is a whole dollar amount.