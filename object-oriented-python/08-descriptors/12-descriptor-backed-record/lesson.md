---
title: Initialize a descriptor-backed record
slug: descriptor-backed-record
order: 12
language: python
lesson_type: coding
summary: A character-stat record uses the same managed rule for maximum health and maximum mana. Route construction through the public fields so new records receive the same validation as later updates.
seo_title: Initialize a descriptor-backed record | Object-oriented Python
seo_description: A character-stat record uses the same managed rule for maximum health and maximum mana. Route construction through the public fields so new records receive the same validation as later updates.
seo_keywords:
  - Python
  - descriptor backed record
  - object-oriented programming
hints:
  - Assign self.max_health and self.max_mana rather than backing dictionary keys.
---

A character-stat record uses the same managed rule for maximum health and maximum mana. Route construction through the public fields so new records receive the same validation as later updates.

A descriptor setter runs on ordinary assignment whether that assignment appears in client code, a method, or `__init__`. The initializer should therefore use public managed attributes when it wants the descriptor's validation. Writing directly into backing storage skips that interface and can admit values a normal update would reject.

The supplied `Positive` descriptor is complete. It remembers each field name, returns per-instance data, and rejects invalid numbers before writing. Your record uses two distinct instances of that descriptor class, so maximum health and maximum mana have separate storage. Different records also have separate dictionaries. These fields describe maximum capacities, not current health or mana: zero is invalid, and fractional capacities are allowed by this model.

The example uses a property to show the same initialization principle in a familiar form. `self.value = value` goes through its setter. Your exercise applies the principle to reusable descriptor objects rather than repeating a property for each field. There is no need to duplicate the checks in the initializer.

When an initializer raises, the class call fails instead of returning a successfully constructed record. The exercise does not require rolling back a partly initialized object: callers receive the exception. For successfully constructed objects, later writes continue to use the same validation policy.

Keep the model an ordinary class here. A descriptor-backed record does not have to be a dataclass. That distinction keeps constructor behavior explicit while you connect the protocol pieces from this module. The probe constructs two characters, updates one stat, and shows that the other record keeps its original value.

## A small example

```python
class InventoryCount:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new):
        if new < 0:
            raise ValueError("Negative inventory count")
        self._value = new

print(InventoryCount(4).value)
```

## Your Tasks

1. Complete `CharacterStats.__init__(max_health, max_mana)` by assigning both arguments through the matching public descriptor fields, so construction applies the supplied `Positive` validation.

Edit `main.py`, then press Run to inspect the supplied probe. Submit checks the task with additional cases. You do not need to change the probe.
