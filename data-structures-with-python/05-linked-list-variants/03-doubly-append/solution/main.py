from __future__ import annotations

class DoubleNode:

    def __init__(self: DoubleNode, value: object) -> None:
        self.value: object = value
        self.prev: DoubleNode | None = None
        self.next: DoubleNode | None = None

class DoublyList:

    def __init__(self: DoublyList) -> None:
        self.head: DoubleNode | None = None
        self.tail: DoubleNode | None = None
        self.size: int = 0

    def prepend(self: DoublyList, value: object) -> DoubleNode:
        node = DoubleNode(value)
        node.next = self.head
        if self.head is None:
            self.tail = node
        else:
            self.head.prev = node
        self.head = node
        self.size += 1
        return node

    def append(self: DoublyList, value: object) -> DoubleNode:
        node = DoubleNode(value)
        node.prev = self.tail
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1
        return node
if __name__ == '__main__':
    try:
        history = DoublyList()
        history.append('Home')
        history.append('Archive')
        print(history.tail.value, history.tail.prev.value)
    except NotImplementedError as error:
        print(error)
