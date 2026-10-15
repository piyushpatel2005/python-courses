---
title: Reject an invalid lobby size
slug: raise-a-built-in-error
order: 1
language: python
lesson_type: coding
summary: Keep a lobby slot count positive without losing its last valid value.
seo_title: Reject an invalid lobby size | Python OOP practice
seo_description: Keep a lobby slot count positive without losing its last valid value.
seo_keywords:
  - Python
  - raise a built in error
  - object oriented programming
hints:
  - Put the guard before the assignment to self.slots.
---

# Reject an invalid lobby size

Mosslight Studio needs Lantern Vale lobbies to reject invalid slot counts. If a host tries to set the count to zero, the lobby should keep its previous setting.

An exception ends the current operation and gives its caller a reason it could not finish. `ValueError` fits a value that has the expected kind but is outside the allowed range. Check before assigning the attribute: a failed update must leave the old count intact. For this exercise, callers supply integers; type validation is outside this method's contract.

Try a valid update first, then an invalid one on the same object. If you assign before checking, the error can appear correct even though the object now holds a bad slot count. A caller should be able to catch the error and continue using the lobby.

## A smaller example

A lantern brightness setting rejects values below its allowed minimum before returning them.

```python
def lantern_brightness(value):
    if value < 0:
        raise ValueError("below the allowed minimum")
    return value
```

## Your Tasks

1. Implement `Lobby.set_slots(count)`: raise `ValueError("slots must be positive")` when `count <= 0`; otherwise store `count` in `self.slots`. Leave the old value unchanged on rejection.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. A finished method prints `Slots: 4`. Press **Submit** to check the behavior with other inputs.
