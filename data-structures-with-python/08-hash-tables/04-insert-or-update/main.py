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
        bucket_index("", capacity)
        self.buckets: list[list[tuple[str, object]]] = [[] for _ in range(capacity)]
        self.size: int = 0

    def put(self, key: str, value: object) -> None:
        # TODO: complete the numbered steps for this function.
        bucket = self.buckets[bucket_index(key, len(self.buckets))]
        for i, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                return None
        return None


def validate_capacity(capacity: int) -> None:
    if type(capacity) is not int or capacity <= 0:
        raise ValueError("capacity must be a positive integer")


if __name__ == "__main__":
    try:
        table = HashTable(1)
        table.put("bolt", 4)
        table.put("nut", 6)
        table.put("bolt", 9)
        print(table.buckets, table.size)
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
