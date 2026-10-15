---
title: Bound methods
slug: bound-methods
order: 1
language: python
lesson_type: coding
summary: Complete `deferred_use(item)` to return the bound `record_use` method of the supplied item without calling it.
seo_title: Bound methods | Python OOP practice
seo_description: Complete `deferred_use(item)` to return the bound `record_use` method of the supplied item without calling
  it.
seo_keywords:
- Python OOP
- bound methods
- coding practice
---

# Bound methods

A menu can save an item action to run after the player selects it. Retrieve the bound method now without activating the item yet. The saved method remembers which item should receive the later call.

## Accessing is different from calling

```python
class Chime:
    def __init__(self, sound):
        self.sound = sound

    def ring(self):
        return self.sound

chime = Chime("ding")
action = chime.ring
print(action())  # ding
```

`chime.ring` has no parentheses. It retrieves a **bound method**, a callable value that combines the method's function with the instance `chime`. Later, `action()` invokes that function with `chime` supplied as `self`.

By contrast, `action = chime.ring()` calls the method immediately and saves its returned string. A string is not the pending operation. This distinction matters when handing work to menus, schedulers, or ordinary functions that will call it later.

A bound method remembers the object, not a frozen copy of its attributes. If you change `chime.sound` before calling `action`, the method reads the changed sound. Two chimes produce bound methods attached to different receivers even though they share the same method definition.

You can also access the function through the class. For this ordinary instance method, `Chime.ring(chime)` explicitly supplies the receiver that `chime.ring()` supplies automatically. Usually the instance-call form is clearer, but the comparison explains where `self` comes from.

The supplied `GameItem.record_use` changes a count and returns the updated count. Complete `deferred_use(item)` so it returns that item's bound method without running it. The probe prints the count before calling the saved operation, then prints the result afterward. If the first count has already increased, the operation happened too early.

## Picture the behavior

The diagram follows `item.record_use()`. A bound method keeps both the receiver and the function: `__self__` is `item`, and `__func__` is `GameItem.record_use`. Calling the saved method supplies the item automatically, just as `GameItem.record_use(item)` would. These names let you inspect the saved action; you do not need to set them.

![The bound method item.record_use remembers item as its receiver and GameItem.record_use as its function; calling it supplies item automatically.](bound-method-self.svg)

## Your Tasks

1. Complete `deferred_use(item)` to return the bound `record_use` method of the supplied item without calling it.

## Run and check

Edit `main.py`. Press **Run** to inspect the supplied console probe, then **Submit** to check your implementation. The completed probe prints a count of `3` before the action and `4` afterward.
