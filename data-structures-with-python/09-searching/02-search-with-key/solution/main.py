from __future__ import annotations
from collections.abc import Callable

def search_with_key(
    records: list[object],
    target: object,
    key: Callable[[object], object],
) -> int:
    for i, record in enumerate(records):
        if key(record) == target:
            return i
    return -1


if __name__ == "__main__":
    try:
        records = [("crate", 4), ("box", 9), ("bag", 4)]
        print(search_with_key(records, 4, lambda row: row[1]))
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
