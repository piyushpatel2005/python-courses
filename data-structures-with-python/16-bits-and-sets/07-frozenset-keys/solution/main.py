from __future__ import annotations
from collections.abc import Hashable, Iterable

def count_bundles(requests: Iterable[Iterable[Hashable]]) -> dict[frozenset[Hashable], int]:
    counts = {}
    for request in requests:
        key = frozenset(request)
        counts[key] = counts.get(key, 0) + 1
    return counts
if __name__ == '__main__':
    try:
        print('Bundle count:', count_bundles([[1, 2], [2, 1]]).get(frozenset([1, 2])))
    except (NotImplementedError, AttributeError, TypeError, IndexError) as error:
        print(error)
