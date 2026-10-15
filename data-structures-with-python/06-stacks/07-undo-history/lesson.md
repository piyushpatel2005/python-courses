---
title: "Restore the last saved text state"
slug: "undo-history"
order: 7
language: "python"
runtime: pyodide
lesson_type: "coding"
summary: "Implement `UndoHistory.undo()` to restore the most recently saved text using the supplied Stack and return `True`, or return `False` without change when no saved state exists."
seo_title: "Restore the last saved text state | Python data structures"
seo_description: "Implement `UndoHistory.undo()` to restore the most recently saved text using the supplied Stack and return `True`, or return `False` without change when no saved state exists."
seo_keywords:
  - "Python"
  - "undo history"
  - "data structures"
---

# Restore the last saved text state

Undo must reverse the most recent change first. A stack of previous states captures that ordering naturally. This lesson adds a supplied UndoHistory wrapper around the completed Stack; you implement only its undo operation.

The constructor stores the current text and a fresh previous-state stack. The supplied replace method pushes the old text before installing the new text. That ordering is important: saving the new text would make undo restore the state already visible. Replacements may repeat the same string, and each replacement still counts as a separate event.

Undo first checks whether a prior state exists. If so, pop the latest saved string, assign it to text, and return True. If the stack is empty, return False and keep the current text. An empty string is a valid saved state, not evidence that history is exhausted. Decide from the stack length rather than the truthiness of the value popped.

Do not call replace from undo. Replace records a new prior state, which would push the state being undone straight back into history. Undo restores without recording another edit. This simple model has no redo branch; a later replacement records the currently restored text as the next undo point.

Strings are immutable, so the history can safely retain references to them. A history of mutable documents would need a snapshot policy or reversible commands; merely storing references would not freeze their earlier contents. The lesson keeps that separate design problem out of the implementation.

## Trace it first

Start with "rough", replace with "edited", then "final". The saved stack is `["rough", "edited"]`, while current text is "final". One undo restores "edited"; another restores "rough". A third returns False and leaves "rough" visible.

## Cost

With immutable strings stored by reference, undo is amortized O(1). The stack stores O(k) references for k saved states, plus the retained string data. It does not copy all text during undo.

## Operation contract

Implement `UndoHistory.undo()` to restore the most recently saved text using the supplied Stack and return `True`, or return `False` without change when no saved state exists.

![Before: current text = ink+line+dot: ('ink', 'ink+line'). Saved text states, oldest → newest. undo() returns True; text = ink+line: ('ink'). Pop the latest saved state; do not save again. undo() returns True; text = ink: (). History is now empty. Next undo() returns False: (). Current text remains ink; no mutation.](stacks-undo-history-trace.svg)

A saved empty string is valid, not an empty stack. Original illustrative example; not exercise input.

## Your Tasks

1. Implement `undo()` to restore the most recent saved text state.

## Run and check

Edit `UndoHistory.undo` in `main.py`. The earlier definitions and Run probe are supplied. Run the completed operation to see:

```text
True revised
```

Press **Submit** to check the tasks on additional inputs and boundary cases.
