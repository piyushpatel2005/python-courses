---
title: "Auxiliary space in a single scan"
slug: auxiliary-space
order: 9
language: python
runtime: pyodide
lesson_type: coding
summary: "Implement `extremes(values)` in one loop with constant auxiliary storage, returning `None` for empty input and otherwise `(lowest, highest)`."
seo_title: "Auxiliary space in a single scan | Python data structures"
seo_description: "Practice auxiliary space through a focused Python implementation, concrete traces, and boundary checks."
seo_keywords:
  - Python
  - auxiliary space
  - data structures practice
---

# Auxiliary space in a single scan

A temperature summary needs only its lowest and highest reading. Keeping a second list of every reading would make the result correct, but it would use storage the summary does not need. Practice maintaining a small amount of state while visiting the input once.

## Keep only what the answer needs

Write `extremes(values)` for an iterable of bounded-size numbers. It returns `(lowest, highest)`, or `None` if the iterable is empty. Begin with a flag indicating that no reading has arrived. The first reading establishes both extremes. Each later reading can replace the lowest, the highest, or neither.

Do not start both extremes at zero. That would incorrectly report zero as the minimum of an all-positive input or as the maximum of an all-negative input. Initializing from the first real reading avoids inventing a value that the sensor never measured.

```python
lowest = 12
next_reading = 7
if next_reading < lowest:
    lowest = next_reading
print(lowest)  # 7
```

The invariant after each iteration is that the two stored values summarize exactly the readings already visited. Equal readings do not require an update. This invariant remains true even if values arrive from an iterator that cannot be restarted.

![Extremes scan over unchanged input \[4,7,2,9\] keeps low/high pairs (4,4), (4,7), (2,7), (2,9). It returns (2,9) without copying the input; empty input returns None and a singleton returns its value twice.](memory-and-cost-auxiliary-space-trace.svg)

Each pair summarizes the readings visited so far without retaining a second collection.

## Input, output, and auxiliary storage

The caller may already own an O(n) input list. That does not make this algorithm's auxiliary space O(n): auxiliary space means extra working storage used by the algorithm. A flag and two references occupy O(1) space independent of the number of readings. The fixed-size result tuple also uses constant space. Runtime is O(n), with at most two comparisons for each reading after the first.

Use a single explicit loop. Do not convert the input to a list, sort it, or delegate to `min` and `max`. Those approaches either keep unnecessary storage, require repeated traversal, or skip the state-maintenance practice. Leave the caller's data unchanged. This lesson measures algorithmic storage, not exact interpreter bytes, and assumes comparisons of individual numbers have bounded cost.

The parameter hint `Iterable[int]` means an object that yields integers in a loop, such as a list or iterator. It is imported from `collections.abc`; the operation does not need indexed access or a known length.

## Build in small steps

The loop, first-reading flag, empty-result behavior, and tuple return are supplied. Initialize from one real reading first, then add the two independent comparison updates.

## Your Tasks

1. Initialize both extremes from the first reading.
2. Replace `low` when a later reading is smaller.
3. Replace `high` when a later reading is larger.

## Run and check

Edit `main.py`, then press **Run** to inspect the supplied probe. Press **Submit** to check the operation on additional inputs. You do not need to copy code from another lesson.
