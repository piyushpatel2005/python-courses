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


if __name__ == "__main__":
    try:
        q = RingQueue(3)
        print(q.data, q.head, q.size)
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
