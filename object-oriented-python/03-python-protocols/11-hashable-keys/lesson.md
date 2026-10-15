---
title: "Build a safe hashable key"
slug: "hashable-keys"
order: 11
language: "python"
lesson_type: "coding"
summary: "Hash the same immutable fields that define value equality."
seo_title: "Build a safe hashable key | Object-oriented Python"
seo_description: "Hash the same immutable fields that define value equality."
seo_keywords: ["python", "hashable keys", "object oriented programming"]
hints: ["Use hash on the pair of fields, not on the display text or object identity."]
---

# Build a safe hashable key

The save registry needs a stable key for a profile and slot number. The supplied `SaveSlotKey` already compares those fields; complete its hash method so an equal fresh key finds the same entry. The registry is an in-memory dictionary.

A hash is an integer used to narrow the search for a key. `hash(value)` calls `__hash__`. Equal objects must have equal hashes. The reverse is not required: different objects may share a hash, so a dictionary still checks equality. Never test that every unequal key produces a different hash, and never depend on a particular numeric hash across Python processes.

The fields involved in equality and hashing must stay stable while an object is a key. Changing a hash after insertion can make a dictionary search in the wrong place. A tuple of immutable values is a useful combined hash input: it preserves field boundaries and lets Python combine their hashes. In this lesson profile is a string and number is an integer, both immutable.

The starter supplies an immutability shell so the task stays focused. `__slots__` reserves one storage attribute; it is explained properly in the next module. `object.__setattr__` performs the initial assignment, while the supplied `__setattr__` and `__delattr__` reject later changes with `AttributeError`. An exception stops an invalid operation; the errors module returns to that idea. The read-only properties expose the tuple's fields. The initializer also rejects a second initialization of the same object. This protects ordinary use, not deliberate bypasses through low-level methods. Leave this shell unchanged.

The tiny example uses a built-in tuple as a dictionary key. Your exercise gives a named object the same stable-key behavior. It is not safe to copy this hash method onto a mutable class such as the earlier save slot.

Submit checks lookup by an equal fresh key and verifies that attempted mutation cannot change the original. Your contribution is the hash policy, not a cached arbitrary identifier.

## A small example

```python
locations = {("east", 6): "spare lamps"}
lookup = tuple(["east", 6])
print(locations[lookup])
```

## Your Tasks

1. Implement `SaveSlotKey.__hash__` by hashing the tuple `(profile, number)`, the same immutable fields used for equality. Keep the supplied immutability and equality code unchanged.

Edit `main.py` and use Run to inspect the supplied check. Leave that check unchanged; Submit tests your method with other values too.
