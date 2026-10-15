---
title: "Delete and compact the occupied prefix"
slug: delete-and-compact
order: 4
language: python
runtime: pyodide
lesson_type: coding
summary: "Implement `Array.delete(index)` to return the removed reference, compact leftward, clear the spare tail slot, and keep capacity unchanged."
seo_title: "Delete and compact the occupied prefix | Python data structures"
seo_description: "Practice delete and compact through a focused Python implementation, concrete traces, and boundary checks."
seo_keywords:
  - Python
  - delete and compact
  - data structures practice
---

# Delete and compact the occupied prefix

Deleting an element leaves a gap in an array's occupied prefix. Close that gap by moving every later reference one position left, then clear the newly unused last slot. This stage completes the small array's basic mutation operations.

## Save the value before shifting

All previous methods are supplied unchanged. `delete(index)` accepts integer indices zero through size - 1 and raises `IndexError` otherwise. Validate first so a failed deletion leaves storage untouched. Save the removed reference before overwriting its slot; the method must return that exact object, not a copy.

Move the suffix from left to right: destination index receives source index + 1, then the next destination receives its right neighbor. This direction is safe because each source has not yet been overwritten. It is the reverse of the safe direction for insertion.

```python
slots = ["L", "M", "N", None]
removed = slots[1]
slots[1] = slots[2]
slots[2] = None
print(removed, slots)  # M ['L', 'N', None, None]
```

The example removes a middle entry. Your method generalizes to every valid position. After shifting, decrease size and set `_data[size]` to `None`. Clearing that slot releases the model's extra reference to the old tail. A snapshot alone would hide a stale reference beyond size, so preserve the whole storage invariant.

![Deleting index 1 from \[4,9,6,2\] removes 9. References 6 and 2 shift one position left, then the last slot is cleared; size becomes three. Deleting the last element requires no shifts.](arrays-and-sequences-delete-and-compact-trace.svg)

The compacted prefix ends one slot earlier, but clearing the old tail does not shrink the storage block.

## Keep capacity on deletion

This class does not shrink its block when deleting. Capacity and `_data` identity remain unchanged, including when the final element is removed. Future insertions can reuse spare slots. A legitimate payload may itself be `None`; the saved reference must still be returned and size must still decrease.

Deleting at index i shifts size - i - 1 references. Removing the last item needs no shifts and takes O(1); removing from the front is O(n). The operation uses O(1) auxiliary space because it keeps only the removed reference and a loop index. Use indexed assignments rather than Python list `pop`, `remove`, slicing, or rebuilding storage. Those shortcuts would avoid the compaction practice or change the modeled slot count.

After this stage, access, append, insert, and delete all agree on one invariant: occupied elements form the prefix before size, and spare slots remain available after it.

## Build in small steps

The starter saves the removed reference for you. Validate and compact first. Then make three small changes: reduce size, clear the newly unused slot, and return the saved reference. Each check creates a fresh array and inspects only the next state change; it never borrows state from an earlier check.

## Your Tasks

1. Reject invalid indices with `IndexError` before accessing or changing storage.
2. Shift later references left to close the gap.
3. Decrease size after compaction.
4. Clear the newly spare tail slot to `None`.
5. Return the saved removed reference.

## Run and check

Edit `main.py`, then press **Run** to inspect the supplied probe. Press **Submit** to check the operation on additional inputs. You do not need to copy code from another lesson.
