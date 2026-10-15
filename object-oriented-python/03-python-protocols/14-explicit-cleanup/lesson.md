---
title: "Keep cleanup explicit"
slug: "explicit-cleanup"
order: 14
language: "python"
lesson_type: "coding"
summary: "Explore __del__ safely without relying on garbage-collection timing."
seo_title: "Keep cleanup explicit | Object-oriented Python"
seo_description: "Explore __del__ safely without relying on garbage-collection timing."
seo_keywords: ["python", "explicit cleanup", "object oriented programming"]
hints: ["The cleanup policy already lives in close; the hook only delegates."]
---

# Keep cleanup explicit

A Lantern Vale play session needs an explicit end point. This exercise models `GameSession` with a closed flag and an event list, without opening files or connections. Connect its finalization hook to the supplied cleanup method, then inspect the hook through a direct call.

`__del__` is a finalization hook. Python may call it as an object is being finalized, but programs must not depend on when that happens, or assume it will happen before shutdown. Different runtimes and reference cycles can change timing. `del name` removes a reference; it does not promise immediate cleanup or an immediate call to `__del__`. Another reference may still keep the object alive.

The starter therefore supplies `close()`. It changes `closed` once and records a single event. Repeating `close()` is harmless; this property is called idempotence. Production code should prefer an explicit call at a known point or a context manager. A context manager's `with` block arranges a deterministic exit action when control leaves the block, including exceptional exits; it does not wait for garbage collection. Implementing that protocol is outside this task.

The small example demonstrates deliberate state change with an ordinary method. No disappearing variable is needed. Your exercise's `__del__` simply delegates to the session's existing `close()` method. A finalizer should not contain important game rules, assume external services remain available, or be the only protection against leaking a resource.

The Run probe calls `session.__del__()` explicitly while the object is still alive. That is an educational inspection of the hook, not a cleanup recommendation and not evidence about automatic finalization. It then calls `close()` again to expose duplicate cleanup. The tests use the same explicit approach, with no garbage-collector calls, sleeps, or timing assumptions.

## A small example

```python
class Indicator:
    def __init__(self):
        self.on = True

    def turn_off(self):
        self.on = False

lamp = Indicator()
lamp.turn_off()
print(lamp.on)
```

## Your Tasks

1. Implement `GameSession.__del__` by calling the supplied idempotent `close()` method. The explicit hook probe and repeated close calls must record only one `closed:<name>` event per session; do not add timing or garbage-collection code.

Edit `main.py` and use Run to inspect the supplied check. Leave that check unchanged; Submit tests your method with other values too.
