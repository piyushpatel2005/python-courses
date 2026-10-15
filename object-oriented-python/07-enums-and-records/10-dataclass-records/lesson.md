---
title: Describe a small dataclass record
slug: dataclass-records
order: 10
language: python
lesson_type: coding
summary: A player save record needs an ordinary object with a player name and an experience count. A dataclass can generate repetitive record methods from field declarations.
seo_title: Describe a small dataclass record | Object-oriented Python
seo_description: A player save record needs an ordinary object with a player name and an experience count. A dataclass can generate repetitive record methods from field declarations.
seo_keywords:
  - Python
  - dataclass records
  - object-oriented programming
hints:
  - Add the decorator above the class and annotated fields inside it.
---

A player save record needs an ordinary object with a player name and an experience count. A dataclass can generate repetitive record methods from field declarations.

Import `dataclass` from `dataclasses` and place `@dataclass` above a class. Inside it, an annotation such as `label: str` declares a field. The decorator uses those annotations to generate an initializer, a readable representation, and value-based equality unless you override the defaults.

A field without a default becomes a required constructor argument. A field with `= value` gains a default. Put required fields before fields with defaults so the generated initializer has a valid parameter order. In the example, callers may omit the second argument but must provide the first.

Annotations describe intended types; they do not automatically reject wrong types at runtime. `count: int` is not a validation check. Likewise, a normal dataclass is mutable: assigning a different field value after construction is allowed. Later exercises can add explicit policies when they need them.

The generated equality compares the field values of instances of the same class. It does not make every independently created record the same object. Two equal records can still be updated independently. Here the fields are a string and an integer, so there is no shared mutable collection to manage. This record models save data in memory; creating it does not write a save file.

Your starter imports the decorator but leaves the record unfinished. Add the decorator and field declarations rather than hand-writing equivalent methods. The supplied probe constructs two records, prints one, and compares them so the generated behavior is visible.

## A small example

```python
from dataclasses import dataclass

@dataclass
class InventoryStack:
    item_name: str
    count: int = 1

print(InventoryStack("Moonstone"))
print(InventoryStack("Moonstone") == InventoryStack("Moonstone"))
```

## Your Tasks

1. Define `PlayerSave` as a dataclass with required `player_name: str` and optional `experience: int = 0`, using generated initialization and equality.

Edit `main.py`, then press Run to inspect the supplied probe. Submit checks the task with additional cases. You do not need to change the probe.
