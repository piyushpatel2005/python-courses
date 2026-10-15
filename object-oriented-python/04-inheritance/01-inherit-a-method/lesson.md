---
title: "Inherit an existing method"
slug: "inherit-a-method"
order: 1
language: "python"
lesson_type: "coding"
summary: "Create a subclass that reuses its base initializer and behavior."
seo_title: "Inherit an existing method | Object-oriented Python"
seo_description: "Create a subclass that reuses its base initializer and behavior. Practice with runnable Python code and behavioral checks."
seo_keywords: ["python", "inherit a method", "object oriented programming"]
hints: ["Put the base class in parentheses after the new class name."]
---

# Inherit an existing method

A refrigerated locker is still a locker. Before adding specialized behavior, establish that relationship so the new class can reuse the existing location label. This first inheritance exercise requires a class declaration, not a copied method.

In `class Child(Parent):`, the class in parentheses is the base class and the new class is a subclass. When Python cannot find an ordinary method on the subclass, it searches its bases. The method is not pasted into every subclass definition. That shared lookup means a later correction to the base behavior can benefit subclasses that have not overridden it.

An inherited instance method still receives the actual instance as `self`. Calling `child.label()` therefore reads the child's stored data even when the method was defined in the parent. If the subclass does not supply `__init__`, it also inherits an initializer. You can construct the subclass using the arguments expected by that inherited initializer.

The example uses two kinds of document rather than storage equipment. `Note` has no new body behavior, so `pass` is sufficient. Its object still gets a title and can call `heading`. In your exercise, keep the same idea: the new class should not duplicate the parent's code just to make a method available.

Inheritance expresses an is-a relationship, not merely a desire to borrow a convenient function. A refrigerated locker can be used where an ordinary locker is expected for labeling purposes. A delivery van that contains a locker would be a different relationship, which the composition lesson will address.

`isinstance(instance, Base)` accepts instances of subclasses as well as the base itself. `issubclass(Child, Base)` asks about the classes. Submit checks that relationship and varies the locker identifier. A hardcoded label or a separate lookalike class would not demonstrate inherited behavior.

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

1. Define `ColdLocker` as a subclass of the supplied `Locker`, inheriting its initializer and `label()` method without redefining either method.

Edit `main.py`, then press Run to inspect the supplied probe. A `Not ready` message means the unfinished operation raised an exception; it does not complete the task. Press Submit to check the behavior with additional values. You do not need to edit the probe.
