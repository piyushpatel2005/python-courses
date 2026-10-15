---
title: "Combine small inherited capabilities"
slug: "multiple-inheritance"
order: 10
language: "python"
lesson_type: "coding"
summary: "Use two bases with distinct stateless methods."
seo_title: "Combine small inherited capabilities | Object-oriented Python"
seo_description: "Use two bases with distinct stateless methods. Practice with runnable Python code and behavioral checks."
seo_keywords: ["python", "multiple inheritance", "object oriented programming"]
hints: ["The concrete class owns the data; its two bases supply the capabilities."]
---

# Combine small inherited capabilities

An inventory card needs a printable identifier and a tracking URL. Those are separate small capabilities, and the supplied classes already implement them without owning initialization. Combine them in one card through multiple inheritance.

Python permits several bases in a class declaration: `class Child(First, Second):`. The child can inherit methods from both. The order of bases matters when more than one class supplies the same attribute, but this exercise avoids a conflict by giving each capability a distinct method name. The next lesson inspects how Python resolves the general case.

A small class intended to contribute reusable behavior is often called a mixin. That word describes a design role, not special Python syntax. These mixins expect the consuming object to have a `code` field. The concrete card owns that field and its initializer; the mixins simply read it. State expectations should be documented so combining classes does not become guesswork.

The example combines two independent text features. Neither has an initializer, so the final class does not need to coordinate competing setup routines. Your card similarly owns its setup in one place. Multiple inheritance involving initializers takes more care; the cooperative diamond lesson will introduce a compatible calling pattern rather than relying on accidental argument agreement.

Do not copy the methods into the card class. Inheriting them keeps each capability's definition in one location and demonstrates lookup across both bases. Composition could also solve many such problems, especially when collaborators have their own state or lifetimes. Use multiple inheritance here because the exercise deliberately models small capabilities of the same object.

The tests check both behaviors with different codes and verify the declared base order. A class that happens to return matching strings without inheriting the capabilities would miss the requested relationship. The observable result should come from the same card instance through two inherited method names.

## A small example

```python
class LoudText:
    def loud(self):
        return "HELLO"

class QuietText:
    def quiet(self):
        return "hello"

class Voice(LoudText, QuietText):
    pass

voice = Voice()
print(voice.loud(), voice.quiet())
```

## Your Tasks

1. Change the supplied `InventoryCard` declaration to inherit from `PrintableCode` then `TrackableCode`, in that order. Keep its initializer and inherit `print_label()` and `tracking_path()` without redefining them.

Edit `main.py`, then press Run to inspect the supplied probe. A `Not ready` message means the unfinished operation raised an exception; it does not complete the task. Press Submit to check the behavior with additional values. You do not need to edit the probe.
