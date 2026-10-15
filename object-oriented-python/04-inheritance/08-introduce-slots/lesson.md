---
title: "Reserve attributes with slots"
slug: "introduce-slots"
order: 8
language: "python"
lesson_type: "coding"
summary: "Declare a fixed attribute layout and reject accidental extra fields."
seo_title: "Reserve attributes with slots | Object-oriented Python"
seo_description: "Declare a fixed attribute layout and reject accidental extra fields."
seo_keywords: ["python", "introduce slots", "object oriented programming"]
hints: ["Declare the names in the class body; do not change the initializer."]
---

# Reserve attributes with slots

A map cell should hold exactly a row and column. A typo such as `cell.colum = 8` should fail instead of creating an unrelated field. Use `__slots__` to give `MapCell` a fixed layout.

Ordinary user-defined instances usually store their attributes in a dictionary named `__dict__`. A class-level `__slots__` declaration names storage locations instead. For a plain class whose bases do not already supply a dictionary, declaring slots without `__dict__` prevents arbitrary additional attributes. The initializer can still assign the listed fields normally.

Use a tuple of attribute-name strings. Those names describe storage, not the values to put there. They belong in the class body, alongside methods, rather than inside `__init__`. A slotted field remains mutable unless you add a separate policy; slots do not freeze an object or validate whether a coordinate is positive.

The example reserves one field for a dial. Its initializer and later reassignment use familiar dot notation. The exercise needs two fields, so your declaration must include both. Omitting one makes the supplied initializer fail with `AttributeError`, which reports an unavailable attribute. Assigning an unlisted name raises the same exception. The later errors module covers catching and designing exceptions in more depth.

Slots can reduce per-instance overhead when many small objects exist, but this lesson makes no particular memory or speed promise. The visible benefit here is a constrained layout. They also affect subclass behavior, which the next lesson handles; do not assume a parent's slots automatically restrict every future subclass.

Keep the coordinate initializer unchanged. Run prints the valid fields and attempts one extra field inside a supplied try/except probe. Before your change that extra assignment succeeds; afterward the probe should report that it was rejected. Submit also confirms that the two legitimate fields can still be updated.

## A small example

```python
class Dial:
    __slots__ = ("position",)

    def __init__(self, position):
        self.position = position

control = Dial(3)
control.position = 5
print(control.position)
```

## Your Tasks

1. Add `__slots__` to `MapCell` for exactly `row` and `column`, without an instance dictionary. Both fields must remain assignable, while extra attributes raise `AttributeError`.

Edit `main.py` and use Run to inspect the supplied check. Leave that check unchanged; Submit tests your method with other values too.
