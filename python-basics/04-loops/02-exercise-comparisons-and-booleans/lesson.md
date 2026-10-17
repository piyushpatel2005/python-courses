---
title: "Exercise: Check Gate Supplies"
slug: exercise-comparisons-and-booleans
order: 2
language: python
lesson_type: coding
summary: Store comparison and logical results for a gate supply check.
seo_title: Python Boolean Expressions Exercise | Python Basics
seo_description: Write comparisons using and, or, and not to check lantern oil and gate keys.
seo_keywords: [python boolean exercise, comparison expressions, logical operators]
---

Write the checks a gate needs before someone enters. It requires enough oil and at least one key. You will also record whether supplies are missing and whether the gate is open.

In **main.py**, `oil_units` and `key_count` are supplied numbers; `gate_closed` is a supplied boolean. Leave them in place. Replace one placeholder assignment at a time, keeping the print calls so you can see each result.

## Your Tasks

1. Set `enough_oil` using a comparison that checks whether `oil_units` is at least `4`.
2. Set `can_enter` using `and` to check that `enough_oil` is true and `key_count` is at least `1`.
3. Set `needs_supplies` using `or` to check whether `oil_units` is below `4` or `key_count` equals `0`.
4. Set `gate_open` using `not` to reverse `gate_closed`.

Press **Run** after each change, then **Submit**. The completed output is `True`, `True`, `False`, `False`, one per line. Write expressions using the variables, not fixed `True` or `False` answers: the checks must also work when the supplies change.

Next, an `if` statement will use a boolean result to choose an action.
