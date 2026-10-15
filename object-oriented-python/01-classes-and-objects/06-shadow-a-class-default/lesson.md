---
title: Shadow a class default
slug: shadow-a-class-default
order: 6
language: python
lesson_type: coding
summary: Complete `set_cooldown(item, turns)` to set that item's own `cooldown_turns` to `turns`, leaving `GameItem.cooldown_turns` and other
  items unchanged.
seo_title: Shadow a class default | Python OOP practice
seo_description: Complete `set_cooldown(item, turns)` to set that item's own `cooldown_turns` to `turns`, leaving `GameItem.cooldown_turns`
  and other items unchanged.
seo_keywords:
- Python OOP
- shadow a class default
- coding practice
---

# Shadow a class default

A particular item needs a longer cooldown than the default. Give that instance its own setting without changing other items. Python calls this **shadowing** a class attribute: the instance value takes precedence when you read it.

## The nearest value wins

```python
class Spell:
    duration_turns = 2

spark = Spell()
flare = Spell()
flare.duration_turns = 10
print(spark.duration_turns)  # 2
print(flare.duration_turns)   # 10
print(Spell.duration_turns)     # 2
```

The assignment through `flare` stores an instance attribute. Reads from that object now find its own value before consulting the class. Nothing was removed from `Spell`; the original default is still there for objects without an override.

Writing `Spell.duration_turns = 10` would be a different operation. It changes the shared class attribute, affecting objects that still rely on it. The object before the dot determines where the assignment goes, so keep your attention on that part of the expression.

A later change to `Spell.duration_turns` does not replace `flare.duration_turns`. The flare already has its own value. You can think of the class setting as a fallback, not as a broadcast that overwrites every instance.

The supplied `set_cooldown(item, turns)` function receives an item and its new cooldown. Set that number of turns directly; do not add it to the current value. The caller has already chosen the full duration.

Only the received item should change. The probe creates two items and customizes one, then prints both values and the class default. Reading all three is more revealing than reading only the customized item: a mistaken class assignment can make that one reading look correct while changing every other item as well.

## Your Tasks

1. Complete `set_cooldown(item, turns)` to set that item's own `cooldown_turns` to `turns`, leaving `GameItem.cooldown_turns` and other items unchanged.

## Run and check

Edit `main.py`. Press **Run** to inspect the supplied console probe, then **Submit** to check your implementation. The completed probe prints `Cooldown turns: 14 7 7`.
