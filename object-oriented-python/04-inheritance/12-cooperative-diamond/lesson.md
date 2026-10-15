---
title: "Cooperate through a diamond"
slug: "cooperative-diamond"
order: 12
language: "python"
lesson_type: "coding"
summary: "Forward one compatible method call through the MRO exactly once."
seo_title: "Cooperate through a diamond | Object-oriented Python"
seo_description: "Forward one compatible method call through the MRO exactly once. Practice with runnable Python code and behavioral checks."
seo_keywords: ["python", "cooperative diamond", "object oriented programming"]
hints: ["Preserve the events argument and let super() choose the next class."]
---

# Cooperate through a diamond

A report build should record its signing step, dating step, and shared document step once each. The hierarchy is a diamond, so directly calling both parents risks visiting the common ancestor twice. Repair the unfinished cooperative method using the MRO instead.

`super()` does not mean a permanently fixed parent. Within `Signed`, it means continue after `Signed` in the actual instance's MRO. For a plain `Signed` instance, the next class is `Document`. For `Report(Signed, Dated)`, the next class is `Dated`, which then continues to `Document`. The current instance travels through the whole chain; Python does not create separate parent instances.

Every participating method must use a compatible signature and forward the same agreed arguments. Here all `build` methods accept `self, events`; `events` is one shared list, and each method appends its own label before delegating. The root method terminates the chain because `object` has no `build` method. This deliberately narrow signature avoids introducing keyword-consumption patterns before they are needed.

The example uses ordinary functions to show ordered forwarding with a shared list. The exercise replaces that explicit function relationship with cooperative method lookup. Append before calling onward to get outer-to-inner order. Calling onward first would reverse the position of that method's event.

Your task changes only `Signed.build`; the other participants already cooperate. Do not call `Document.build` or `Dated.build` by name. A fixed call would skip or repeat work when the same mixin appears in a different hierarchy. Call the next implementation once and return its result.

The tests use the report, a plain signed document, and a reversed sibling order. This exposes hardcoded routes that happen to fit one diamond. No initializer chain is involved here: the lesson isolates cooperative method signatures and lookup before adding stateful construction complexity.

## A small example

```python
def finish(events):
    events.append("finished")
    return events

def prepare(events):
    events.append("prepared")
    return finish(events)

print(prepare([]))
```

## Picture the behavior

This smaller diamond uses letter names to make the lookup order visible. The arrows show the order of lookup, not direct parent relationships. Your report chain stops at its root `build` method, before `object`, which has no `build`.

![The example diamond has MRO D, B, C, A, object; super inside B continues at C on a D instance.](cooperative-mro-order.svg)

## Your Tasks

1. Implement `Signed.build(events)` to append `signed`, call the next `build(events)` through `super()` exactly once, and return that call's result. It must cooperate in both sibling orders and when used alone.

Edit `main.py`, then press Run to inspect the supplied probe. A `Not ready` message means the unfinished operation raised an exception; it does not complete the task. Press Submit to check the behavior with additional values. You do not need to edit the probe.
