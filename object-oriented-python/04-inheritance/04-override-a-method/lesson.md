---
title: "Override one behavior"
slug: "override-a-method"
order: 4
language: "python"
lesson_type: "coding"
summary: "Replace an inherited method without changing the caller interface."
seo_title: "Override one behavior | Object-oriented Python"
seo_description: "Replace an inherited method without changing the caller interface."
seo_keywords: ["python", "override a method", "object oriented programming"]
hints: ["Define the replacement on LightBeacon, not on Beacon."]
---

# Override one behavior

A light beacon marks a location without a sound cue. Both beacon types answer `signal()`, but return different text. Override that behavior while leaving the shared location setup in the base class; no audio or graphics are involved.

An override is a method defined in a subclass with the same name as an inherited method. Lookup finds the subclass version first, so calls on the specialized instance use that implementation. The base method still exists and still serves ordinary base instances; overriding does not edit it globally.

Keep the public calling convention compatible. If callers already use `beacon.signal()` with no extra arguments, the override should accept that same call. Requiring a new positional argument would make the subclass harder to substitute. The method should also keep returning a string rather than printing, because callers may collect or format the message.

The example changes the sound of an instrument. It does not duplicate the instrument's initializer, and its replacement method reads the inherited instance field. Your quiet beacon should do the same with its stored location. You are changing a policy, not the object's ability to hold its own data.

An override may replace the behavior completely or extend it. This lesson is a complete replacement; the next one uses `super()` to reuse a base result before adding a detail. Do not call the old signal merely out of habit when its loud wording is exactly what you intend to replace.

After Run, construct both beacon types for the same location. Their messages should differ while their stored locations match. Submit varies the location and confirms that the base beacon remains unchanged. That second check catches an easy mistake: editing the supplied base method rather than specializing the subclass.

## A small example

```python
class Instrument:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f"{self.name}: ring"

class Drum(Instrument):
    def sound(self):
        return f"{self.name}: tap"

print(Drum("small drum").sound())
```

## Your Tasks

1. Override `LightBeacon.signal()` to return `Light at <location>` using the inherited location field. Leave the base beacon and inherited initializer unchanged.

Edit `main.py` and use Run to inspect the supplied check. Leave that check unchanged; Submit tests your method with other values too.
