---
title: Delete a managed value
slug: descriptor-delete
order: 5
language: python
lesson_type: coding
summary: A cached label should be removable without removing its field definition. Add a deletion hook that clears only the selected record's stored value.
seo_title: Delete a managed value | Object-oriented Python
seo_description: A cached label should be removable without removing its field definition. Add a deletion hook that clears only the selected record's stored value.
seo_keywords:
  - Python
  - descriptor delete
  - object-oriented programming
hints:
  - Use pop with a default on the instance dictionary.
---

A cached label should be removable without removing its field definition. Add a deletion hook that clears only the selected record's stored value.

The statement `del record.field` invokes a descriptor's `__delete__(self, instance)` when that hook is defined on its type. The operation removes or resets the managed value according to your policy. It does not delete the descriptor object from the owner class.

This exercise chooses an idempotent policy: deleting an already empty field is harmless, and a later read returns `None`. A dictionary's `pop(key, default)` is useful here. It removes and returns the stored item if present, or returns the default if absent. Without a default, a missing key would raise `KeyError`.

The example demonstrates `pop` on ordinary storage. Your descriptor receives the owner through `instance`, so its dictionary is the one to edit. Deleting `self.key` or modifying the descriptor's own dictionary would affect the field configuration instead of the selected record's data.

The supplied getter and setter already use a backing key. Reuse that same key in the deletion hook. Do not call `del instance.label` inside the hook for `label`: that would re-enter the managed deletion operation rather than clear its underlying data.

Follow the probe through a write, a delete, and a read. The second record should retain its value throughout. After deletion, the first record should still accept a new assignment because the descriptor remains attached to the class. These are separate observations of one deletion behavior, not separate features to implement.

## A small example

```python
storage = {"_draft": "Map revision"}
removed = storage.pop("_draft", None)
print(removed)
print(storage.pop("_draft", None))
```

## Your Tasks

1. Implement `CachedLabel.__delete__` to remove `self.key` from the selected instance dictionary if present, without raising for an absent value.

Edit `main.py`, then press Run to inspect the supplied probe. Submit checks the task with additional cases. You do not need to change the probe.
