---
title: "Exercise: Check Gate Readiness"
slug: exercise-logical-operators
order: 4
language: python
lesson_type: coding
summary: "Use and, or, and not to combine gate-supply checks."
seo_title: "Python Logical Operators Exercise | Python Basics"
seo_description: "Practice and, or, and not with supplied oil, keys, and gate state."
seo_keywords: [python logical operators exercise, boolean expressions, gate supplies]
---

The gate needs enough oil **and** a key before someone can enter. It also needs to report if **either** supply is missing. Finally, its open state is the opposite of its closed state.

The supplied `oil_units`, `key_count`, and `gate_closed` are your inputs. `enough_oil` already compares oil with the minimum, as you did two lessons ago. Replace each placeholder in `main.py` with an expression using the named values. A fixed `True` or `False` will not work when the inputs change.

## Your Tasks

1. Set `can_enter` using `and` to require `enough_oil` and `key_count >= 1`.
2. Set `needs_supplies` using `or` to check `oil_units < 4` or `key_count == 0`.
3. Set `gate_open` using `not` to reverse `gate_closed`.

Press **Run** after each edit and **Submit** to check it. For the supplied values, the three new lines print `True`, `False`, `False`. Completing one task should earn its check even while the other placeholders remain unfinished. Next, `if` will use these boolean results to choose a route.
