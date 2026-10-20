---
title: "Exercise: Pack Boxes with while"
slug: exercise-while
order: 2
language: python
runtime: pyodide
lesson_type: coding
summary: "Count packing rounds with a bounded while loop."
seo_title: "Python while Loop Exercise | Python Basics"
seo_description: "Use while and += to pack boxes in batches until a target count is reached."
seo_keywords: [python while exercise, loop counter, packing boxes]
---

A shop has packed 10 boxes and wants 40 ready for pickup. Each packing round adds 10 boxes. The starter supplies `boxes_packed` and `packing_rounds`; the latter starts at zero.

Use `while boxes_packed < 40:` to check the count before every round. Inside the loop, add 10 to the boxes and one to the round count. At 40 the condition becomes false. If 40 boxes had already been packed, the body would not run. `+=` adds to a variable, much as the countdown used `-=` to subtract.

## Your Tasks

1. Add a `while` loop that raises `boxes_packed` by 10 and `packing_rounds` by 1 until 40 boxes are packed.

Place your loop above the supplied, unindented print calls in `main.py`. **Run** should print `40` then `3` on separate lines. Press **Submit** when it does.
