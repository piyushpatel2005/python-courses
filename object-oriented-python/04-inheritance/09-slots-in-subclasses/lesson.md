---
title: "Keep slots in a subclass"
slug: "slots-in-subclasses"
order: 9
language: "python"
lesson_type: "coding"
summary: "Add only new subclass slots without restoring an instance dictionary."
seo_title: "Keep slots in a subclass | Object-oriented Python"
seo_description: "Add only new subclass slots without restoring an instance dictionary."
seo_keywords: ["python", "slots in subclasses", "object oriented programming"]
hints: ["Inherited slots already exist; list only label on the subclass."]
---

# Keep slots in a subclass

A named waypoint needs the base waypoint's x and y fields plus a label. The base already uses slots, but inheritance alone does not keep the subclass restricted. Declare only the new storage the subclass needs.

A subclass that omits `__slots__` normally gains an instance dictionary, even when its parent has none. That dictionary allows extra attributes again. To preserve a fixed layout, a subclass can declare slots for its new fields. When it adds no fields, `__slots__ = ()` is the empty-tuple form that prevents adding a dictionary at that level.

Inherited slots remain available. Do not repeat their names in the child declaration. Repeating a name creates a separate slot descriptor that hides the inherited one and makes the layout confusing. The child's declaration should list only storage newly owned by the child. Its initializer can still call `super().__init__` to fill the base slots, then assign its extra field.

The example below makes a specialized flag with no additional state. The empty declaration is intentional, not an unfinished body. Your exercise differs: the subclass really needs one new field, so an empty tuple would make its initializer fail when it tries to store that field.

Slots control attribute storage, not privacy or immutability. The inherited coordinates and new label can all be changed after construction. An unlisted field should raise `AttributeError`, meaning that assignment cannot target an available attribute. If some base already provides `__dict__`, adding slots later does not remove that inherited dictionary; the supplied base avoids that situation.

The probe builds a named waypoint and tries an extra note. The tests check the class declaration as well as behavior, so repeating all three field names is not an acceptable shortcut. Keep ownership visible: the base owns coordinates, and the subclass owns the label.

## A small example

```python
class Flag:
    __slots__ = ("raised",)

    def __init__(self, raised):
        self.raised = raised

class SignalFlag(Flag):
    __slots__ = ()

print(SignalFlag(True).raised)
```

## Your Tasks

1. Give `NamedWaypoint` a `__slots__` declaration containing only `label`. Preserve inherited x/y storage, allow updates to all three fields, and prevent arbitrary extra attributes.

Edit `main.py` and use Run to inspect the supplied check. Leave that check unchanged; Submit tests your method with other values too.
