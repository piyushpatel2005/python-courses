---
title: "Slide a fixed-width sum"
slug: sliding-window
order: 6
language: python
runtime: pyodide
lesson_type: coding
summary: "Implement `max_window_sum(values, width)` with one initial sum loop and constant-work rolling updates; reject invalid widths with `ValueError`."
seo_title: "Slide a fixed-width sum | Python data structures"
seo_description: "Practice sliding window through a focused Python implementation, concrete traces, and boundary checks."
seo_keywords:
  - Python
  - sliding window
  - data structures practice
---

# Slide a fixed-width sum

A monitoring report needs the largest total across any k consecutive readings. Adding all k values again for each starting position repeats most of the work. A sliding window updates the current total by removing the outgoing reading and adding the incoming one.

## Keep the window's meaning precise

For a window ending just before index end, the total describes exactly the k positions before end. Build the first window's total with a loop over its k values. Initialize the best total to that real window total, not zero; an all-negative input still has a largest window, and its sum may be negative.

When moving right by one, subtract the value at end - k and add the value at end. The new total describes the next window. Compare it with the best seen so far. After processing the final entering value, every full-width window has been considered once.

```python
readings = [5, -2, 8, 1]
current = readings[0] + readings[1] + readings[2]
next_total = current - readings[0] + readings[3]
print(current, next_total)  # 11 7
```

The example moves one width-three window. Your loop must handle all starts and every valid width. A width of one examines individual readings; a width equal to the list length has only one window. Empty input has no valid positive-width window.

![Three width-three windows over \[4,1,7,2,6\] have sums 12,10,15. Shifting subtracts 4 and adds 2, then subtracts 1 and adds 6. The maximum is 15; the array does not change.](arrays-and-sequences-sliding-window-trace.svg)

The middle window has a smaller total, so keep the best seen so far even while the current total falls.

## Validate before reading

Write a fresh `max_window_sum(values, width)` function for integer lists and integer widths. Raise `ValueError` unless `1 <= width <= len(values)`. Do not mutate the input. Return only the best sum, so equal best windows require no tie-breaking rule.

The first sum costs O(k). Each remaining window costs constant arithmetic work, for O(n) time overall and O(1) auxiliary space under the bounded-integer model. Repeated slices and `sum` calls would cost O(nk) in the worst case. Use explicit initialization and rolling updates rather than those shortcuts. This pattern differs from a two-pointer reversal: both boundaries here move in the same direction while the window width stays fixed.

## Build in small steps

The two loops, best-total initialization, and return are supplied. After validating widths, make the first-window sum correct. The final task reuses that sum for each entering value rather than rebuilding windows.

## Your Tasks

1. Raise `ValueError` unless the width fits a nonempty window.
2. Build the first window total in the supplied initialization loop.
3. Slide the total by one position and update `best` when it improves.

## Run and check

Edit `main.py`, then press **Run** to inspect the supplied probe. Press **Submit** to check the operation on additional inputs. You do not need to copy code from another lesson.
