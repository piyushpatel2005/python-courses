from __future__ import annotations

from typing import Any, Callable, Iterable

def stable_key_sort(records: list[Any], key: Callable[[Any], Any]) -> list[Any]:
    result = list(records)
    for index in range(1, len(result)):
        insert_record(result, index, key)
    return result

def shift_records(records: list[Any], index: int, item_key: Any, key: Callable[[Any], Any]) -> int:
    # TODO task 1: In `shift_records`, shift records with larger keys and return the gap position.
    raise NotImplementedError('Complete this step')

def insert_record(records: list[Any], index: int, key: Callable[[Any], Any]) -> None:
    # TODO task 2: In `insert_record`, fill the returned gap with the saved original record.
    item = records[index]
    cursor = shift_records(records, index, key(item), key)
    raise NotImplementedError('Fill the record gap')

if __name__ == "__main__":
    try:
        records = [(3, "fern"), (1, "reed"), (3, "moss")]
        print(stable_key_sort(records, lambda row: row[0]))
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
