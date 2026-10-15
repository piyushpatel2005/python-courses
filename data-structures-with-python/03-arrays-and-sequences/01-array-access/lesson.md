---
title: "Array access and occupied positions"
slug: array-access
order: 1
language: python
runtime: pyodide
lesson_type: coding
summary: "Implement `Array.get(index)` to return the referenced occupied value and raise `IndexError` for negative or out-of-range integer indices."
seo_title: "Array access and occupied positions | Python data structures"
seo_description: "Practice array access through a focused Python implementation, concrete traces, and boundary checks."
seo_keywords:
  - Python
  - array access
  - data structures practice
---

# Array access and occupied positions

An array separates the position of an element from the element itself. Our small `Array` class models indexed storage with a Python list of slots. Begin by reading an occupied position without scanning the whole structure.

## Size is not capacity

The supplied constructor copies its input references into `_data`, stores the occupied count in `size`, and records the number of available slots in `capacity`. Capacity is at least one even for an empty array. Unoccupied positions contain `None`. The invariant is `0 <= size <= capacity` and `len(_data) == capacity`; valid elements occupy exactly the prefix before size.

This is an explicit educational model, not access to CPython's actual allocator. The Python list underneath is a convenient way to represent slots. Its own implementation may reserve additional memory, which is outside our model. Each occupied slot stores a reference, so copying the container does not clone mutable payload objects.

```python
slots = ["north", "south", None, None]
occupied = 2
print(slots[1])             # south
print(1 < occupied)         # True
print(3 < occupied)         # False
```

The last slot exists physically in this model but is not an occupied element. A `None` value can also be a legitimate occupied payload; determine validity by the index and size, never by checking whether the stored value is `None`.

## A precise access contract

Implement `get(index)` for integer indices. Accept zero through size - 1 and raise `IndexError` otherwise. Unlike ordinary Python lists, this teaching class deliberately rejects negative indices. Check before indexing so a negative index cannot accidentally read a spare slot from the end. Access must not change size, capacity, or stored values.

The supplied `snapshot()` returns a shallow list of occupied values for inspection. It costs O(n), whereas `get` uses one slot access and costs O(1). This distinction is why tests read individual positions rather than requiring a printed representation. `Any` in payload annotations means this model accepts arbitrary objects; it does not claim that those objects support arithmetic. Later stages preserve this constructor and completed methods while adding one operation at a time.

## Build in small steps

The constructor and snapshot method are supplied. Validate the integer index first; this check does not need a completed read. The second change is a single indexed return.

## Your Tasks

1. Reject invalid indices with `IndexError` before accessing or changing storage.
2. Return the reference at the validated index.

## Run and check

Edit `main.py`, then press **Run** to inspect the supplied probe. Press **Submit** to check the operation on additional inputs. You do not need to copy code from another lesson.
