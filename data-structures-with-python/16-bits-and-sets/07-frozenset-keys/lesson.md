---
title: "Use an unordered group as a key"
slug: "frozenset-keys"
order: 7
language: "python"
runtime: pyodide
lesson_type: "coding"
summary: "Count equivalent groups with immutable frozenset dictionary keys."
seo_title: "Use an unordered group as a key | Python data structures"
seo_description: "Count equivalent groups with immutable frozenset dictionary keys."
seo_keywords:
  - "Python"
  - "use an unordered group as a key"
  - "bits and sets"
---

# Use an unordered group as a key

A room-booking report groups requests by their equipment requirements. A request for a screen and a speaker describes the same bundle as a request for a speaker and a screen. Repeated equipment names inside one request should not change that bundle.

A tuple preserves order, so it does not directly express this identity rule. An ordinary set does express membership, but it is mutable and cannot be a dictionary key. `frozenset` is an immutable set. When all its members are hashable, the frozenset is hashable too and can serve as a key.

## Separate bundle identity from frequency

Convert each request into a frozenset, then increment the dictionary count for that key. Duplicates inside a request disappear during conversion. Duplicate requests do not disappear: each is another booking and increments its bundle's frequency. These are two different levels of duplication.

Suppose the requests are `['screen', 'speaker']`, `['speaker', 'screen', 'screen']`, and `[]`. The first two share a key and together have count two. The last contributes one occurrence of the empty frozenset. Empty requirements are a legitimate bundle, not a missing request.

Use a new result dictionary for each function call. Never sort or modify the caller's inner lists just to make their keys comparable. Creating a frozenset takes a membership snapshot; later appending an item to the original list must not change an existing key. This is a shallow snapshot of hashable members, not a deep copy of arbitrary objects.

For r requests containing m listed members in total, construction takes expected O(r+m) work under ordinary hashing assumptions. The r term matters when many requests are empty. Storage includes the distinct group memberships and their counts. Long or expensive-to-hash members add their own cost. Frozensets are appropriate when order and multiplicity inside a group are intentionally irrelevant; use a different key if either matters.

The imported hint `Iterable` means an input you can loop over, and `Hashable` describes members usable in a set or dictionary key. Square brackets state the contained type. These hints allow strings or integers without pretending that mutable lists can be set members.

## Small example

```python
first = frozenset(["screen", "speaker"])
second = frozenset(["speaker", "screen", "screen"])
print(first == second)
print({first: 2}[second])
```

Expected output:

```text
True
2
```

## Supplied setup

The dictionary, loop, and return are supplied. The temporary assignment of count 1 lets you check key construction before implementing frequency accumulation.

## Your Tasks

1. Convert each request to a frozenset key, ignoring its order and inner duplicates.
2. Accumulate the number of requests for each key instead of overwriting its count.

## Run and check

Edit `main.py`, then press **Run** to inspect the supplied probe. Press **Submit** to check the operation on changed inputs and boundary cases. The probe is supplied. Complete the numbered steps in order; Submit checks each step separately.
