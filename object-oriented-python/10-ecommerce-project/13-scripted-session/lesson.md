---
title: Run a scripted shopping session
slug: scripted-session
order: 13
language: python
lesson_type: coding
summary: Process a list of console commands while recovering from expected user errors.
seo_title: Run a scripted shopping session | Python OOP practice
seo_description: Process a list of console commands while recovering from expected
  user errors.
seo_keywords:
  - Python
  - scripted session
  - object oriented programming
hints:
  - Put try/except inside the loop so one bad command does not end the session.
---

# Run a scripted shopping session

Process a list of console commands while recovering from expected user errors.

A scripted session makes the command-line workflow repeatable without blocking on `input()`. The caller supplies a Shop and an iterable of command strings. Return one response per attempted command. Catch `ValueError` and `KeyError` at this user-facing boundary, prefixing their text with `Error: `. Other failures should still be visible to a developer. A stripped command equal to `quit` ends the session without adding a response.

A bad command does not discard earlier responses. Append its error message at the same position and move on to the next command. By contrast, quit is a control command: it adds no response and stops consuming the remaining iterable. This separation makes a transcript easy to inspect.

## A smaller example

The word loop stops before recording the stop marker or anything after it.

```python
responses = []
for word in ["north", "stop", "south"]:
    if word == "stop":
        break
    responses.append(word.upper())
print(responses)
```

## Your Tasks

1. Implement `run_session(shop, commands)` to collect `shop.execute` responses in order until stripped `quit`. Convert only `ValueError` and `KeyError` into `"Error: " + str(error)` and continue; propagate other errors. Empty input returns an empty list.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. The finished responses show an addition, creation of `O1`, and its placed status. Press **Submit** to check the behavior with other inputs.
