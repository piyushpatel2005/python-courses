---
title: "Inherit an existing method"
slug: "inherit-a-method"
order: 1
language: "python"
lesson_type: "coding"
summary: "Create a subclass that reuses its base initializer and behavior."
seo_title: "Inherit an existing method | Object-oriented Python"
seo_description: "Create a subclass that reuses its base initializer and behavior."
seo_keywords: ["python", "inherit a method", "object oriented programming"]
hints: ["Put the base class in parentheses after the new class name."]
---

# Inherit an existing method

The protocol methods gave game objects familiar Python behavior. Now Mosslight Studio needs related objects to share behavior: a `SupplyChest` is a `GameEntity`, so it should inherit the existing entity label. Start with the subclass declaration rather than copying a method.

In `class Child(Parent):`, the class in parentheses is the base class and the new class is a subclass. When Python cannot find an ordinary method on the subclass, it searches its bases. The method is not pasted into every subclass definition. That shared lookup means a later correction to the base behavior can benefit subclasses that have not overridden it.

An inherited instance method still receives the actual instance as `self`. Calling `child.label()` therefore reads the child's stored data even when the method was defined in the parent. If the subclass does not supply `__init__`, it also inherits an initializer. You can construct the subclass using the arguments expected by that inherited initializer.

The example uses two kinds of document rather than game entities. `Note` has no new body behavior, so `pass` is sufficient. Its object still gets a title and can call `heading`. In your exercise, keep the same idea: the new class should not duplicate the parent's code just to make a method available.

Inheritance expresses an is-a relationship, not merely a desire to borrow a convenient function. A supply chest can be used wherever the game expects an entity label. An inventory that contains a chest has a different relationship, which the composition lesson will address.

`isinstance(instance, Base)` accepts instances of subclasses as well as the base itself. `issubclass(Child, Base)` asks about the classes. Submit checks that relationship and varies the game entity identifier. A hardcoded label or a separate lookalike class would not demonstrate inherited behavior.

## A small example

```python
class Document:
    def __init__(self, title):
        self.title = title

    def heading(self):
        return self.title.upper()

class Note(Document):
    pass

print(Note("reminder").heading())
```

## Your Tasks

1. Define `SupplyChest` as a subclass of the supplied `GameEntity`, inheriting its initializer and `label()` method without redefining either method.

Edit `main.py` and use Run to inspect the supplied check. Leave that check unchanged; Submit tests your method with other values too.
