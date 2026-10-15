from __future__ import annotations
from collections.abc import Hashable, Iterable

def compare_groups(left: Iterable[Hashable], right: Iterable[Hashable]) -> dict[str, set[Hashable]]:
    a, b = (set(left), set(right))
    return {'either': a | b, 'both': a & b, 'left_only': a - b, 'exclusive': a ^ b}
if __name__ == '__main__':
    try:
        print('Group comparison:', compare_groups([2, 4, 4], [4, 9]))
    except (NotImplementedError, AttributeError, TypeError, IndexError) as error:
        print(error)
