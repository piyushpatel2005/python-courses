---
title: "Compose a service from a collaborator"
slug: "compose-a-service"
order: 7
language: "python"
lesson_type: "coding"
summary: "Delegate formatting to an injected object rather than inheriting it."
seo_title: "Compose a service from a collaborator | Object-oriented Python"
seo_description: "Delegate formatting to an injected object rather than inheriting it."
seo_keywords: ["python", "compose a service", "object oriented programming"]
hints: ["Read self.formatter on every call so collaborator replacement takes effect."]
---

# Compose a service from a collaborator

The quest HUD uses a formatter, but it is not a formatter. Store that helper on `QuestHUD` and ask it to format each message. The HUD here is a text-only object, so you can replace its helper without building a UI or another inheritance tree.

The supplied `QuestHUD` initializer receives a formatter object and stores it as `self.formatter`. Passing a dependency into an object instead of constructing it internally is often called dependency injection. Here it is just an ordinary constructor argument. The benefit is concrete: the caller can supply a different formatter while the HUD keeps the same publishing behavior.

Your publishing method should ask the stored collaborator to format the incoming text and pass its result back to the caller. The HUD does not need to know the formatter's concrete type or how it builds the text. It only relies on the small interface: a `format` method accepting one text argument and returning a string.

The example shows a playlist containing a speaker. The playlist calls a method on that separate object; it does not inherit from the speaker. Notice the two dots in `self.speaker.play(title)`: first retrieve the collaborator, then call its behavior. The exercise uses that same relationship with text formatting rather than playback.

Inheritance is still useful when a specialized object can stand in for its base. Composition is useful when responsibilities are separate or the collaborator may vary independently. Do not make `QuestHUD` a subclass of its formatter simply to reach the `format` method.

The tests pass different collaborators and replace one on an existing HUD. They also count calls to detect duplicate formatting. Do not create a new `BracketFormatter` inside `publish`, because doing so would ignore the supplied dependency and make replacement ineffective. The returned message should come directly from the current collaborator.

## A small example

```python
class Speaker:
    def play(self, title):
        return f"Playing {title}"

class Playlist:
    def __init__(self, speaker):
        self.speaker = speaker

    def start(self, title):
        return self.speaker.play(title)

print(Playlist(Speaker()).start("Rain"))
```

## Picture the behavior

The diagram uses a separate example: `MatchService` asks an injected `ScoreRule` for `score(points)`. Your `QuestHUD` delegates text formatting instead. Both examples keep the helper separate from its caller and run entirely in memory.

![MatchService delegates score(points) to an injected ScoreRule without inheriting from it.](composed-service-delegation.svg)

## Your Tasks

1. Implement `QuestHUD.publish(text)` to call the current formatter's `format(text)` exactly once and return its result. Use the injected collaborator instead of constructing or inheriting a formatter.

Edit `main.py` and use Run to inspect the supplied check. Leave that check unchanged; Submit tests your method with other values too.
