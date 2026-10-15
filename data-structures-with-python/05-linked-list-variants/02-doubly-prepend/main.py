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
        raise NotImplementedError('Complete DoublyList.prepend')
if __name__ == '__main__':
    try:
        history = DoublyList()
        history.prepend('Archive')
        history.prepend('Home')
        print(history.head.value, history.tail.prev.value, history.size)
    except NotImplementedError as error:
        print(error)
