---
title: "Demo: Compare Workshop Supplies"
slug: comparisons-and-booleans
order: 1
language: python
lesson_type: coding
summary: Compare supply quantities and combine True-or-False checks before branching.
seo_title: Python Comparisons and Booleans | Python Basics
seo_description: Edit supply values to see comparison operators and and, or, and not produce boolean results.
seo_keywords: [python comparisons, python booleans, logical operators]
---

The **Gate Trials** begin with a comparison. Before a program can choose a route, it needs a way to check a value. Start away from the gate with a community workshop that needs at least five paint tubes.

A comparison returns `True` or `False`, capitalized in Python. `=` assigns a value; `==` compares two values.

| Operator | Meaning |
| --- | --- |
| `==` | equal to |
| `!=` | not equal to |
| `>` | greater than |
| `<` | less than |
| `>=` | greater than or equal to |
| `<=` | less than or equal to |

The editable **main.py** starts with six paint tubes. Its first two checks print `True` and `False`: six is at least five, but is not equal to five.

The remaining lines combine checks about markers and paper. `and` requires both checks to be true; `or` requires at least one. `not` reverses a boolean, so `not (markers == 0)` asks whether the markers have not run out. The parentheses make the check being reversed clear.

Run the starter and read the last three lines: `True`, `False`, and `True`. Then make the two small edits in **main.py**.

## Your Tasks

1. Change `paint_tubes` to `4` while keeping the supplied comparisons. The first two lines should now both be `False`.
2. Change `paper_packs` to `1` while keeping the combined checks. The final three lines should now be `False`, `True`, and `True`.

Press **Run** after each edit, then **Submit**. The next exercise asks you to write checks for different supplies, rather than changing this demo's values.
