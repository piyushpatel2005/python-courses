from __future__ import annotations

class RingQueue:
    data: list[object]
    head: int
    size: int

    def __init__(self, capacity: int) -> None:
        if type(capacity) is not int or capacity <= 0:
            raise ValueError("capacity must be a positive integer")
        self.data: list[object] = [None] * capacity
        self.head: int = 0
        self.size: int = 0

    def enqueue(self, value: object) -> None:
        # TODO: complete the numbered steps for this function.
        return None


if __name__ == "__main__":
    try:
        q = RingQueue(2)
        q.enqueue("north")
        q.enqueue("south")
        print(q.data, q.size)
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
