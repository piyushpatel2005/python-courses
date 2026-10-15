from __future__ import annotations

from typing import Any, Callable, Iterable

def stable_key_sort(records: list[Any], key: Callable[[Any], Any]) -> list[Any]:
    result = list(records)
    for index in range(1, len(result)):
        insert_record(result, index, key)
    return result

def shift_records(records: list[Any], index: int, item_key: Any, key: Callable[[Any], Any]) -> int:
    cursor = index
    while cursor > 0 and item_key < key(records[cursor - 1]):
        records[cursor] = records[cursor - 1]
        cursor -= 1
    return cursor

def insert_record(records: list[Any], index: int, key: Callable[[Any], Any]) -> None:
    item = records[index]
    cursor = shift_records(records, index, key(item), key)
    records[cursor] = item

if __name__ == "__main__":
    try:
        records = [(3, "fern"), (1, "reed"), (3, "moss")]
        print(stable_key_sort(records, lambda row: row[0]))
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
