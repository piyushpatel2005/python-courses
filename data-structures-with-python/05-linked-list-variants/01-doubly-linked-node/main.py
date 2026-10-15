from __future__ import annotations

class DoubleNode:

    def __init__(self: DoubleNode, value: object) -> None:
        self.value: object = None  # TODO: keep the payload reference
        self.prev: DoubleNode | None  # TODO: assign the detached link
        self.next: DoubleNode | None  # TODO: assign the detached link

class DoublyList:

    def __init__(self: DoublyList) -> None:
        self.head: DoubleNode | None = None
        self.tail: DoubleNode | None = None
        self.size: int = 0
if __name__ == '__main__':
    try:
        node = DoubleNode('Archive')
        print(node.value, getattr(node, 'prev', 'unfinished'), getattr(node, 'next', 'unfinished'))
    except NotImplementedError as error:
        print(error)
