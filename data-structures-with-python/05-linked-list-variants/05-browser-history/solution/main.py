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
if __name__ == '__main__':
    try:
        history = BrowserHistory('Home')
        history.visit('Archive')
        history.back()
        history.visit('Contact')
        print(history.current.value, history.pages.size, history.back())
    except NotImplementedError as error:
        print(error)
