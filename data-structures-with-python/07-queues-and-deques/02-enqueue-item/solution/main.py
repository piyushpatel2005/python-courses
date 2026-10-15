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
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size: int = 0

    def enqueue(self, value: object) -> None:
        node = Node(value)
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1


if __name__ == "__main__":
    try:
        q = LinkedQueue()
        q.enqueue("ticket-A")
        q.enqueue("ticket-B")
        print(q.head.value, q.tail.value, q.size)
    except (NotImplementedError, AttributeError, TypeError, IndexError, OverflowError) as error:
        print(error)
