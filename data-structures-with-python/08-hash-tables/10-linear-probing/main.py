from __future__ import annotations

def bucket_index(key: str, capacity: int) -> int:
    validate_capacity(capacity)
    result = 0
    for character in key:
        result = (result * 31 + ord(character)) % capacity
    return result


_DELETED = object()


class ProbingTable:
    slots: list[object]
    size: int

    def __init__(self, capacity: int = 8) -> None:
        bucket_index("", capacity)
        self.slots: list[object] = [None] * capacity
        self.size: int = 0

    def put(self, key: str, value: object) -> None:
        start = bucket_index(key, len(self.slots))
        first_deleted = None
        for offset in range(len(self.slots)):
            index = probe_slot(start, offset, len(self.slots))
            entry = self.slots[index]
            if entry is _DELETED:
                if first_deleted is None:
                    first_deleted = index
            elif entry is None:
                target = index if first_deleted is None else first_deleted
                self.slots[target] = (key, value)
                self.size += 1
                return None
            elif entry[0] == key:
                self.slots[index] = (key, value)
                return None
        if first_deleted is not None:
            self.slots[first_deleted] = (key, value)
            self.size += 1
            return None
        raise OverflowError("full table")

    def get(self, key: str) -> object:
        # TODO: complete the numbered steps for this function.
        start = bucket_index(key, len(self.slots))
        for offset in range(len(self.slots)):
            index = probe_slot(start, offset, len(self.slots))
            entry = self.slots[index]
            if entry is None:
                return None
            if entry is not _DELETED and entry[0] == key:
                return None
        return None


def validate_capacity(capacity: int) -> None:
    if type(capacity) is not int or capacity <= 0:
        raise ValueError("capacity must be a positive integer")


def probe_slot(start: int, offset: int, capacity: int) -> int:
    # TODO: complete the numbered steps for this function.
    return None


if __name__ == "__main__":
    try:
        table = ProbingTable(4)
        table.put("c", 10)
        table.put("g", 20)
        print(table.get("c"), table.get("g"))
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
