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

    def remove(self: DoublyList, node: DoubleNode | None) -> DoubleNode:
        if node is None:
            raise ValueError('A live node is required')
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        self.size -= 1
        node.prev = None
        node.next = None
        return node

class BrowserHistory:

    def __init__(self: BrowserHistory, first_page: str) -> None:
        self.pages: DoublyList = DoublyList()
        self.current: DoubleNode = self.pages.append(first_page)

    def back(self: BrowserHistory) -> str:
        if self.current.prev is not None:
            self.current = self.current.prev
        return self.current.value

    def forward(self: BrowserHistory) -> str:
        if self.current.next is not None:
            self.current = self.current.next
        return self.current.value

    def visit(self: BrowserHistory, page: str) -> str:
        while self.pages.tail is not self.current:
            self.pages.remove(self.pages.tail)
        self.current = self.pages.append(page)
        return page

class RingNode:

    def __init__(self: RingNode, value: object) -> None:
        self.value: object = value
        self.next: RingNode | None = None

class CircularList:

    def __init__(self: CircularList) -> None:
        self.head: RingNode | None = None
        self.tail: RingNode | None = None
        self.size: int = 0

    def append(self: CircularList, value: object) -> RingNode:
        node = RingNode(value)
        if self.head is None:
            self.head = node
            node.next = node
        else:
            node.next = self.head
            self.tail.next = node
        self.tail = node
        self.size += 1
        return node

    def values(self: CircularList) -> list[object]:
        result = []
        current = self.head
        for _ in range(self.size):
            result.append(current.value)
            current = current.next
        return result

    def remove_first(self: CircularList, value: object) -> RingNode | None:
        previous = self.tail
        current = self.head
        for _ in range(self.size):
            if current.value == value:
                if self.size == 1:
                    self.head = None
                    self.tail = None
                else:
                    previous.next = current.next
                    if current is self.head:
                        self.head = current.next
                    if current is self.tail:
                        self.tail = previous
                    self.tail.next = self.head
                self.size -= 1
                current.next = None
                return current
            previous, current = (current, current.next)
        return None

class SkipNode:

    def __init__(self: SkipNode, key: int | None, height: int) -> None:
        if type(height) is not int or height < 1:
            raise ValueError('Height must be a positive integer')
        self.key: int | None = key
        self.forward: list[SkipNode | None] = [None] * height

class SkipList:

    def __init__(self: SkipList, max_level: int=4) -> None:
        if type(max_level) is not int or max_level < 1:
            raise ValueError('max_level must be a positive integer')
        self.max_level: int = max_level
        self.head: SkipNode = SkipNode(None, max_level)
        self.tail: SkipNode | None = None
        self.size: int = 0
if __name__ == '__main__':
    try:
        node = SkipNode(24, 3)
        print(node.key, node.forward)
    except NotImplementedError as error:
        print(error)
