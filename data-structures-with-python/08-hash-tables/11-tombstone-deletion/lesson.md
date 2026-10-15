---
title: "Delete with a tombstone"
slug: "tombstone-deletion"
order: 11
language: "python"
runtime: pyodide
lesson_type: "coding"
summary: "Preserve probe-chain reachability by marking deletion instead of creating an empty slot."
seo_title: "Delete with a tombstone | Data structures with Python"
seo_description: "Preserve probe-chain reachability by marking deletion instead of creating an empty slot."
seo_keywords:
  - Python
  - tombstone deletion
  - data structures
---

The probing constructor, put, and completed get are carried forward unchanged. Add deletion without breaking lookup for keys farther along the same probe sequence.

An untouched `None` slot tells get to stop. If deletion replaced a pair with `None`, a later colliding key could become unreachable even though its pair still exists. A tombstone is a distinct marker meaning "a pair used to occupy this slot; keep searching." This implementation supplies `_DELETED = object()` as that marker. Compare it with `is`, not by a value convention a caller might accidentally store.

For a separate trace, imagine two keys with home slot two stored at slots two and three. After removing the first key, the slot at two must contain the marker. A lookup for the second key skips that marker and reaches slot three. The table's number of live keys decreases, but the search path survives.

Follow the same wrapped, capacity-bounded probe as get. An untouched slot or a complete unsuccessful cycle means return `False`. An equal live key means replace that pair with `_DELETED`, decrement size, and return `True`. A repeated delete returns false without another size change.

The supplied put already supports reuse. It remembers the first tombstone but does not immediately insert there: an equal key might occur later. Updating that later pair must not create a duplicate. If no equal key exists, the saved tombstone becomes reusable, even when no untouched slot remains.

Deletion takes O(capacity) probes in the worst case. Expected short probes need suitable distribution and enough genuinely available space; many tombstones can slow searches even with a small live load factor. Rebuilding can remove those markers, but automatic cleanup is outside this fixed-table exercise.

![With capacity five, linear probing, and integer hash k modulo five, keys 7, 12, and 17 occupy slots 2, 3, and 4. Deleting 12 leaves a tombstone in slot 3. Lookup of 17 checks 2, continues through 3, and matches 4. A miss for 22 continues to never-used slot 0 and stops.](probing-tombstone-search.svg)

This schematic uses integer keys and h(k) = k % 5 to make the probe path easy to follow; your implementation keeps the supplied string hash. In either model, DEL means continue, while an untouched slot ends the search.

## Your Tasks

1. Return `False` when a bounded probe finds no live equal key.
2. Replace an equal live pair with `_DELETED` and return `True`.
3. Reduce size only when a live pair was marked deleted.

Edit `main.py` one step at a time. Run uses the supplied probe; an unfinished field or return value may print a reminder. Submit checks the numbered steps in order, so you can see each completed step before finishing the next.
