---
title: "Shallow copies preserve element references"
slug: shallow-copies
order: 3
language: python
runtime: pyodide
lesson_type: coding
summary: "Implement `copy_outer(items)` to copy only the outer list, preserving every element reference."
seo_title: "Shallow copies preserve element references | Python data structures"
seo_description: "Practice shallow copies through a focused Python implementation, concrete traces, and boundary checks."
seo_keywords:
  - Python
  - shallow copies
  - data structures practice
---

# Shallow copies preserve element references

A dispatch screen needs its own list of delivery cards. Removing a card from the screen should not remove it from the master list, but both screens should still see edits to a shared card. A shallow copy provides exactly this boundary.

## Copy the container, keep the elements

`list(existing)` creates a new list and copies the element references into it. The outer lists are different objects. An element that was mutable remains shared; making the outer copy does not recursively clone everything reachable from it.

```python
record = ["draft"]
original = [record]
view = list(original)
view.append(["extra"])
record[0] = "approved"
print(len(original), original[0])  # 1 ['approved']
print(view[0] is original[0])      # True
```

There are two separate effects. Adding an outer entry changes only `view`. Updating the nested `record` is visible through both outer lists because both still refer to it. Drawing two outer boxes with arrows to the same inner box is often more useful than looking at printed list values.

![Shallow copy: outer lists a and b point to the same inner lists X and Y. Appending 9 through b changes X to \[3, 8, 9\], visible through a too; outer lists remain distinct.](memory-and-cost-shallow-copies-trace.svg)

The separate outer lists still share X, so a nested append is visible through either copy.

## Decide what independence means

Implement `copy_outer(items)` to return a new list containing the same references in the same order. You may use `list`, slicing, or an explicit loop. An empty input still requires a new empty list; returning the input unchanged would violate the contract even when both print as `[]`. Repeated references must remain repeated references, not separate clones.

The work is O(n) because n references must be copied. The new outer container uses O(n) space. These bounds count references, not the sizes of the objects they point to. A list containing a large nested object does not copy that whole object during a shallow copy. The next lesson changes the boundary deliberately by copying each row as well. Neither version promises a fully independent copy of an arbitrary object graph.

## Build in small steps

The starter currently returns an alias. Replace that return expression with an outer copy; do not add a nested-copy operation.

## Your Tasks

1. Return a new shallow copy of `items`.

## Run and check

Edit `main.py`, then press **Run** to inspect the supplied probe. Press **Submit** to check the operation on additional inputs. You do not need to copy code from another lesson.
