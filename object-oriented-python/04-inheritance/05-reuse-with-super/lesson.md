---
title: "Extend a method through super"
slug: "reuse-with-super"
order: 5
language: "python"
lesson_type: "coding"
summary: "Reuse a base result before adding a subclass detail."
seo_title: "Extend a method through super | Object-oriented Python"
seo_description: "Reuse a base result before adding a subclass detail."
seo_keywords: ["python", "reuse with super", "object oriented programming"]
hints: ["super().label() produces the shared text; add only the subclass suffix."]
---

# Extend a method through super

A reward quest needs the ordinary quest label plus its point reward. Rebuilding the whole label would duplicate the base formatting rule. Extend the returned text instead.

You have used `super()` during initialization. The same mechanism works with ordinary methods. `super().label()` looks for the next label implementation after the current class in the actual instance's method resolution order. In this single-inheritance example it reaches `Quest.label`. The method remains bound to the current instance, so it reads that quest's code.

The returned value is ordinary data. Store it in a local variable or combine it directly with the subclass's extra text. The important part is that the base method computes the shared portion. If the base later changes punctuation or adds a prefix, the subclass should inherit that change rather than preserve an outdated copy.

The small example extends a greeting with a time-of-day note. It shows that the subclass can add information without knowing exactly how the base creates its phrase. Your quest uses a different message and a supplied point reward. Keep its initializer; the unfinished behavior is only the label method.

Avoid calling `self.label()` from inside that same override. Lookup would find the override again, causing recursion rather than selecting the base implementation. `super()` changes the starting point of lookup; it does not create a second parent object or change the instance's class.

Submit changes the base label temporarily to confirm that your implementation genuinely reuses it. This is more informative than checking one fixed string, which could pass even if you copied the base's current output format. Reuse should work with arbitrary quest codes and point rewards, without altering either attribute.

## A small example

```python
class Greeting:
    def text(self):
        return "Welcome"

class MorningGreeting(Greeting):
    def text(self):
        return super().text() + " this morning"

print(MorningGreeting().text())
```

## Your Tasks

1. Implement `RewardQuest.label()` by calling `super().label()` once and appending ` | reward <points>` using this instance's points. Keep the shared label policy in the base class.

Edit `main.py` and use Run to inspect the supplied check. Leave that check unchanged; Submit tests your method with other values too.
