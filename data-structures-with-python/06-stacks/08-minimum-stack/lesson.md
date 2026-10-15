---
title: "Remember the minimum at every stack depth"
slug: "minimum-stack"
order: 8
language: "python"
runtime: pyodide
lesson_type: "coding"
summary: "Implement `MinStack.push(value)` for comparable integer values by pushing `(value, minimum_so_far)` onto the supplied entries Stack; return `None` and do not scan older entries."
seo_title: "Remember the minimum at every stack depth | Python data structures"
seo_description: "Implement `MinStack.push(value)` for comparable integer values by pushing `(value, minimum_so_far)` onto the supplied entries Stack; return `None` and do not scan older entries."
seo_keywords:
  - "Python"
  - "minimum stack"
  - "data structures"
---

# Remember the minimum at every stack depth

A regular stack can find its smallest value by scanning all items, but that makes every minimum request linear. Store a small amount of extra information with each pushed value so the answer is already available at the top.

This lesson introduces a supplied MinStack wrapper rather than changing Stack's earlier contracts. Its entries is a Stack of pairs. Each pair contains the original value and the minimum of all values from the bottom through that position. The supplied minimum method reads the second component of the top pair. The supplied pop removes a pair and returns its first component. Both raise IndexError when empty through their explicit check or the underlying Stack.

You implement only push. On an empty stack, the new value is also the minimum so far. Otherwise compare it with the previous top's saved minimum and store the smaller of the two alongside the new value. Use only the previous summary, not a scan of older entries.

Duplicate minima work without a special removal counter. Each depth records its own minimum. Popping one occurrence exposes the previous depth's saved answer, which may contain the same minimum again. Negative values follow the same comparison rule.

The invariant can be checked for every depth: the saved minimum at that position equals the minimum of the prefix ending there. This is an example of augmenting a structure with a summary that can be updated locally. It trades extra storage for faster queries without changing last-in-first-out behavior.

## Trace it first

Push 11, then 4, then 4, then 9. The pairs are `(11,11), (4,4), (4,4), (9,4)`. Popping 9 leaves minimum 4. Popping one 4 still leaves minimum 4. Only after removing the second 4 does the minimum return to 11.

## Cost

Push and pop are amortized O(1) with the list-backed Stack; minimum is O(1). Each position stores one extra reference, so total space remains O(n). Comparisons assume bounded-size integers.

## Operation contract

Implement `MinStack.push(value)` for comparable integer values by pushing `(value, minimum_so_far)` onto the supplied entries Stack; return `None` and do not scan older entries.

![Before: (value, minimum so far): ('9,9', '4,4', '4,4'). Each pair summarizes its entire prefix. push(7): store (7, 4): ('9,9', '4,4', '4,4', '7,4'). minimum() returns 4; push returns None. Pop 7, then pop one 4: ('9,9', '4,4'). The other 4 remains; minimum() is still 4.](stacks-minimum-stack-trace.svg)

Cells show value,minimum; duplicate minima survive. Original illustrative example; not exercise input.

## Your Tasks

1. Implement `MinStack.push(value)` to save a value with its prefix minimum.

## Run and check

Edit `MinStack.push` in `main.py`. The earlier definitions and Run probe are supplied. Run the completed operation to see:

```text
2 9 2
```

Press **Submit** to check the tasks on additional inputs and boundary cases.
