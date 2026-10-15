from __future__ import annotations

class RingQueue:
    data: list[object]
    head: int
    size: int

    def __init__(self, capacity: int) -> None:
        # TODO: complete the numbered steps for this function.
        pass


if __name__ == "__main__":
    try:
        q = RingQueue(3)
        print(q.data, q.head, q.size)
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
