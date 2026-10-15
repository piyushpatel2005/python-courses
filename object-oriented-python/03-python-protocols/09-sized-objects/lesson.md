---
title: "Give an object a length"
slug: "sized-objects"
order: 9
language: "python"
lesson_type: "coding"
summary: "Implement __len__ from the current collection contents."
seo_title: "Give an object a length | Object-oriented Python"
seo_description: "Implement __len__ from the current collection contents. Practice with runnable Python code and behavioral checks."
seo_keywords: ["python", "sized objects", "object oriented programming"]
hints: ["Ask the list for its length each time the method runs."]
---

# Give an object a length

A library cart holds a changing list of titles. Other code should ask `len(cart)` rather than reaching into the cart and counting its internal list itself. Add that small public interface without duplicating stored state.

Python calls `__len__(self)` when it evaluates `len(value)`. The method must return a nonnegative integer. A string such as `"three"`, a floating-point value, or a negative count violates the protocol even if it looks useful to a human. Delegating to the length of an existing list is a reliable way to meet that requirement.

The starter copies the incoming iterable with `list(titles)`. That gives each cart its own list container rather than keeping an alias to the caller's list. The initializer is supplied; your job is only to expose the current number of titles. Do not store a second count in `__init__`: it can become stale after someone appends or removes a title. Compute the answer from the list whenever Python asks.

The small example measures a tuple of coordinates. Python already knows its length; your wrapper will forward a similar request to its own contained collection. Empty collections are worth checking because length zero is a valid answer, not an error or missing result.

Length also participates in truth testing when a class has no `__bool__`. An empty cart will be false and a nonempty cart true once its length method works. The next lesson gives truth testing its own explicit meaning for a different class. Here, counting contents is enough.

After the first Run, append another title to the sample cart and run a fresh length query. The result should change without rebuilding the object. Submit also constructs empty and longer carts so an answer tied to the initial sample cannot satisfy the contract.

## A small example

```python
coordinates = (8, 3)
print(len(coordinates))
print(len(()))
```

## Your Tasks

1. Implement `LibraryCart.__len__` to return the current number of items in `titles`, including zero for an empty cart.

Edit `main.py`, then press Run to inspect the supplied probe. A `Not ready` message means the unfinished operation raised an exception; it does not complete the task. Press Submit to check the behavior with additional values. You do not need to edit the probe.
