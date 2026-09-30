---
title: Number Supply Kits with for and range
slug: number-supply-kits
order: 4
language: python
lesson_type: coding
summary: Use for and range to label a fixed number of workshop supply kits.
seo_title: Python for Loop and range Exercise | Python Basics
seo_description: Use Python for loops and range to generate numbered workshop labels and see why the stop number is excluded.
seo_keywords: [python for loop, python range, loop labels]
hints:
  - range(1, 5) gives 1, 2, 3, 4; the stop value is excluded.
---

# Number supply kits

When the number of repetitions is known, `for` can walk through a `range`. Here is a separate job numbering cleanup bins:

```python
for bin_number in range(1, 4):
    print("Bin", bin_number)
# Bin 1, Bin 2, Bin 3
```

`range(start, stop)` includes the start but **not** the stop. `range(3)` starts at zero. The editor provides an empty label string and prints it afterward. Build labels for four kits without typing each number separately.

## Your Task

1. Write a `for kit_number in range(1, 5)` loop that appends `f"Kit {kit_number}; "` to `labels` on each turn. The supplied print should show four labels.
