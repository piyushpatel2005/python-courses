---
title: "Keep cleanup explicit"
slug: "explicit-cleanup"
order: 14
language: "python"
lesson_type: "coding"
summary: "Explore __del__ safely without relying on garbage-collection timing."
seo_title: "Keep cleanup explicit | Object-oriented Python"
seo_description: "Explore __del__ safely without relying on garbage-collection timing. Practice with runnable Python code and behavioral checks."
seo_keywords: ["python", "explicit cleanup", "object oriented programming"]
hints: ["The cleanup policy already lives in close; the hook only delegates."]
---

# Keep cleanup explicit

A resource owner needs a reliable moment to release what it owns. This lesson uses a simulated lease and an event list, not a real file or network connection. You will connect a finalization hook to an already supplied explicit cleanup method, then observe that hook through a direct call only.

`__del__` is a finalization hook. Python may call it as an object is being finalized, but programs must not depend on when that happens, or assume it will happen before shutdown. Different runtimes and reference cycles can change timing. `del name` removes a reference; it does not promise immediate cleanup or an immediate call to `__del__`. Another reference may still keep the object alive.

The starter therefore supplies `close()`. It changes `closed` once and records a single event. Repeating `close()` is harmless; this property is called idempotence. Production code should prefer an explicit call at a known point or a context manager. A context manager's `with` block arranges a deterministic exit action when control leaves the block, including exceptional exits; it does not wait for garbage collection. Implementing that protocol is outside this task.

The small example demonstrates deliberate state change with an ordinary method. No disappearing variable is needed. Your exercise's `__del__` simply delegates to the lease's existing `close()` method. A finalizer should not contain important business logic, assume external services remain available, or be the only protection against leaking a resource.

The Run probe calls `lease.__del__()` explicitly while the object is still alive. That is an educational inspection of the hook, not a cleanup recommendation and not evidence about automatic finalization. It then calls `close()` again to expose duplicate cleanup. The tests use the same explicit approach, with no garbage-collector calls, sleeps, or timing assumptions.

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

1. Implement `Lease.__del__` by calling the supplied idempotent `close()` method. The explicit hook probe and repeated close calls must record only one `closed:<name>` event per lease; do not add timing or garbage-collection code.

Edit `main.py`, then press Run to inspect the supplied probe. A `Not ready` message means the unfinished operation raised an exception; it does not complete the task. Press Submit to check the behavior with additional values. You do not need to edit the probe.
