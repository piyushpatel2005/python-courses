---
title: Count Arrivals with while
slug: count-arrivals-with-while
order: 3
language: python
lesson_type: coding
summary: Write a bounded while loop that counts arriving workshop guests.
seo_title: Python while Loop Exercise | Python Basics
seo_description: Learn to set a counter, check a while condition, and update it to stop a beginner Python loop.
seo_keywords: [python while loop, counter loop, beginner python loops]
hints:
  - Increase both the number of guests checked and the ticket number inside the loop.
---

# Count arrivals with `while`

A volunteer checks tickets until the numbered queue is done. A `while` loop repeats **as long as** its condition is true:

```python
bag = 1
while bag <= 2:
    print("Inspect bag", bag)
    bag += 1
# Inspect bag 1, then Inspect bag 2
```

The update matters: without `bag += 1`, the condition never becomes false. Use the editor's supplied starting values to check tickets 1 through 3. No keyboard input is needed; you can rerun the fixed queue safely.

## Your Task

1. Write a `while ticket <= 3` loop that adds 1 to `checked` and advances `ticket` by 1 each time. The supplied print should show `3`.
