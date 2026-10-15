---
title: Class defaults
slug: class-defaults
order: 5
language: python
lesson_type: coding
summary: Give `GameItem` a class attribute named `cooldown_turns` with the value `7`. Instances should use that shared default rather
  than store their own copy.
seo_title: Class defaults | Python OOP practice
seo_description: Give `GameItem` a class attribute named `cooldown_turns` with the value `7`. Instances should use that shared default
  rather than store their own copy.
seo_keywords:
- Python OOP
- class defaults
- coding practice
---

# Class defaults

Items share a default cooldown: the number of turns before they can be activated again. For this exercise, that default is seven turns. Store it on the class so items without their own setting all read the same value.

## Data on the class

An assignment directly inside a class body belongs to the class. It is different from assigning through an instance name after construction.

```python
class Spell:
    recharge_turns = 30

spell = Spell()
print(Spell.recharge_turns)  # 30
print(spell.recharge_turns)         # 30
```

For the ordinary attributes in this module, Python checks the instance first. When the instance has no value named `recharge_turns`, lookup continues on its class. The class value is available through the instance, but Python has not copied it into that instance.

That distinction becomes visible when the default changes:

```python
Spell.recharge_turns = 45
print(spell.recharge_turns)  # 45
```

The already-created spell sees the updated default because it still has no individual override. A newly created spell sees it too. This is useful for settings that truly describe the category rather than one particular item.

Keep individual names and usage counts on individual items. If changing one item's name changed every item's name, the data would be stored at the wrong level. A shared integer default works well here; mutable collections such as lists need more care, which you will practice shortly.

The editor supplies an empty `GameItem` class. Put the default assignment in its indented body, where `pass` currently stands. The probe reads the default through both the class and an instance. The tests also change the class default temporarily to check that new and existing items consult the class instead of receiving a copied value.

## Your Tasks

1. Give `GameItem` a class attribute named `cooldown_turns` with the value `7`. Instances should use that shared default rather than store their own copy.

## Run and check

Edit `main.py`. Press **Run** to inspect the supplied console probe, then **Submit** to check your implementation. Both completed readings should be `7`.
