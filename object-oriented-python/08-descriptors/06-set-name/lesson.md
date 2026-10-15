---
title: Let the class supply a field name
slug: set-name
order: 6
language: python
lesson_type: coding
summary: A character loadout has two managed fields for its weapon and armor. Let Python tell each descriptor its public name instead of manually configuring a backing key for every assignment.
seo_title: Let the class supply a field name | Object-oriented Python
seo_description: A character loadout has two managed fields for its weapon and armor. Let Python tell each descriptor its public name instead of manually configuring a backing key for every assignment.
seo_keywords:
  - Python
  - set name
  - object-oriented programming
hints:
  - Use the name parameter; do not hardcode either of the sample field names.
---

A character loadout has two managed fields for its weapon and armor. Let Python tell each descriptor its public name instead of manually configuring a backing key for every assignment.

When a class is created, Python calls `__set_name__(self, owner, name)` on objects in its class namespace that define the hook. `owner` is the newly created class and `name` is the attribute name used in that class body. The hook runs during class creation, before you instantiate a record.

A descriptor often derives a backing key from this name, such as an underscore followed by the public name. The getter and setter can then use that configured key for every owner instance. Two separate descriptor objects receive different names, so they do not overwrite each other's values within one record.

The example only records the name to show when it becomes available. Your exercise uses it to configure storage. The getter and setter are already complete; without the hook they both use the same placeholder key, causing the two fields to collide.

Reuse the descriptor class by constructing a fresh descriptor for each managed attribute. Reusing one descriptor object under two different names would call its hook twice, and a design with only one `self.key` would remember only the last name. Likewise, assigning a descriptor to a class after creation does not automatically call `__set_name__`; you would need to arrange that call yourself.

The exercise stays with normal class-body declarations. Inheritance can reuse those existing descriptors without renaming them, while an unrelated owner class can declare new descriptor objects. The checks exercise both multiple fields and multiple owners, so a fixed backing key is not enough.

## A small example

```python
class Named:
    def __set_name__(self, owner, name):
        self.public_name = name

class SpawnPoint:
    zone = Named()

print(SpawnPoint.zone.public_name)
```

## Your Tasks

1. Implement `NamedField.__set_name__` so `self.key` becomes an underscore followed by the attribute name Python supplies.

Edit `main.py`, then press Run to inspect the supplied probe. Submit checks the task with additional cases. You do not need to change the probe.
