from __future__ import annotations

def bucket_index(key: str, capacity: int) -> int:
    validate_capacity(capacity)
    result = 0
    for character in key:
        result = (result * 31 + ord(character)) % capacity
    return result


class HashTable:
    buckets: list[list[tuple[str, object]]]
    size: int

    def __init__(self, capacity: int = 8) -> None:
        # TODO: complete the numbered steps for this function.
        validate_capacity(capacity)


def validate_capacity(capacity: int) -> None:
    if type(capacity) is not int or capacity <= 0:
        raise ValueError("capacity must be a positive integer")


if __name__ == "__main__":
    try:
        table = HashTable(4)
        print(table.buckets, table.size)
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
