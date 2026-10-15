---
title: Keep descriptor storage per instance
slug: per-instance-storage
order: 4
language: python
lesson_type: coding
summary: Two players share a badge field definition but must not share a stored badge. Move their data into the individual owner objects.
seo_title: Keep descriptor storage per instance | Object-oriented Python
seo_description: Two players share a badge field definition but must not share a stored badge. Move their data into the individual owner objects.
seo_keywords:
  - Python
  - per instance storage
  - object-oriented programming
hints:
  - Store values on instance.__dict__, while self.key only identifies the storage location.
---

Two players share a badge field definition but must not share a stored badge. Move their data into the individual owner objects.

Only one descriptor object is created by an assignment in the owner class body. Every instance normally reaches that same helper. If the setter saves the latest value as `self.value`, the helper has one slot for all owners, so updating one record can affect another.

An ordinary object's `__dict__` holds its instance attributes. Use the `instance` parameter to select the right dictionary. For example, a descriptor can store under `instance.__dict__[self.key]` and retrieve from the same key. The descriptor keeps configuration such as a key name; each owner keeps its own changing data.

The example shows the distinction without a descriptor: two objects have separate dictionaries even when both use the same key string. Your getter and setter will use this same storage arrangement indirectly. A key starting with an underscore is a convention for backing storage, not a security boundary.

This exercise supplies the key `_badge`. Read with `dict.get(key)` so an unwritten field returns `None`, and assign with `dictionary[key] = value` when writing. There is no validation policy here; badges may be any value. The important behavior is isolation and consistent storage.

Both methods belong to one focused repair because together they implement one field-storage contract. Test an interleaved sequence: write one player profile, write another, then read the first again. Reading only the most recently written player profile would miss the shared-storage bug.

## A small example

```python
class InventoryItem:
    pass

first, second = InventoryItem(), InventoryItem()
first.__dict__["_tag"] = "north"
second.__dict__["_tag"] = "south"
print(first.__dict__["_tag"])
```

## Your Tasks

1. Complete `StoredBadge.__get__` and `__set__` to read and write each owner's `__dict__` at `self.key`; unwritten badges should read as `None`.

Edit `main.py`, then press Run to inspect the supplied probe. Submit checks the task with additional cases. You do not need to change the probe.
