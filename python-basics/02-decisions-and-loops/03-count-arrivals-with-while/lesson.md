---
title: Count Gate Pulses with while
slug: count-arrivals-with-while
order: 3
language: python
lesson_type: coding
summary: Write a bounded while loop to count the pulses that charge Ari’s gate.
seo_title: Python while Loop Exercise | Python Basics
seo_description: Practice a terminating Python while loop with beacon pulses.
seo_keywords: [python while loop, counter loop, beginner python loops]
hints:
  - Increase `charged` and `pulse` inside the loop so it terminates.
---

# Count gate pulses with `while`

The gate needs three pulses before its lock releases. A `while` loop repeats **as long as** its condition is true. In another chamber:

```python
spark = 1
while spark <= 2:
    print("Inspect spark", spark)
    spark += 1
# Inspect spark 1, then Inspect spark 2
```

The update matters: without `spark += 1`, the condition never becomes false. Use the supplied starting values in `main.py` to count pulses 1 through 3. No keyboard input is needed.

## Your Task

1. Write a `while pulse <= 3` loop that adds 1 to `charged` and advances `pulse` by 1 each time. Run to see `3`, then Submit.
