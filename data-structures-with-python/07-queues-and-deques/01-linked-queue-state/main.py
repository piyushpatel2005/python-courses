from __future__ import annotations

class Node:
    value: object
    next: Node | None

    def __init__(self, value: object) -> None:
        self.value: object = value
        self.next: Node | None = None


class LinkedQueue:
    head: Node | None
    tail: Node | None
    size: int

    def __init__(self) -> None:
        # TODO: complete the numbered steps for this function.
        pass


if __name__ == "__main__":
    try:
        q = LinkedQueue()
        print(q.head, q.tail, q.size)
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
