---
title: "Give an object a length"
slug: "sized-objects"
order: 9
language: "python"
lesson_type: "coding"
summary: "Implement __len__ from the current collection contents."
seo_title: "Give an object a length | Object-oriented Python"
seo_description: "Implement __len__ from the current collection contents."
seo_keywords: ["python", "sized objects", "object oriented programming"]
hints: ["Ask the list for its length each time the method runs."]
---

# Give an object a length

An inventory holds a changing list of item names. Let the game ask `len(inventory)` instead of counting the internal list itself. The count should stay correct when items are added or removed.

Python calls `__len__(self)` when it evaluates `len(value)`. The method must return a nonnegative integer. A string such as `"three"`, a floating-point value, or a negative count violates the protocol even if it looks useful to a human. Delegating to the length of an existing list is a reliable way to meet that requirement.

The starter copies the incoming iterable with `list(items)`. That gives each inventory its own list container rather than keeping an alias to the caller's list. The initializer is supplied; your job is only to expose the current number of items. Do not store a second count in `__init__`: it can become stale after someone appends or removes an item. Compute the answer from the list whenever Python asks.

The small example measures a tuple of coordinates. Python already knows its length; your wrapper will forward a similar request to its own contained collection. Empty collections are worth checking because length zero is a valid answer, not an error or missing result.

Length also participates in truth testing when a class has no `__bool__`. An empty inventory will be false and a nonempty inventory true once its length method works. The next lesson gives truth testing its own explicit meaning for a different class. Here, counting contents is enough.

After the first Run, append another item to the sample inventory and run a fresh length query. The result should change without rebuilding the object. Submit also constructs empty and longer inventories so an answer tied to the initial sample cannot satisfy the contract.

## A small example

```python
coordinates = (8, 3)
print(len(coordinates))
print(len(()))
```

## Your Tasks

1. Implement `Inventory.__len__` to return the current number of items in `items`, including zero for an empty inventory.

Edit `main.py` and use Run to inspect the supplied check. Leave that check unchanged; Submit tests your method with other values too.
