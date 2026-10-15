from __future__ import annotations

class Node:

    def __init__(self: Node, value: object, next_node: Node | None=None) -> None:
        self.value: object = value
        self.next: Node | None = next_node

def values(head: Node | None) -> list[object]:
    result = []
    current = head
    while current is not None:
        result.append(current.value)
        current = current.next
    return result

class LinkedList:

    def __init__(self: LinkedList) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size: int = 0

    def prepend(self: LinkedList, value: object) -> Node:
        node = Node(value, self.head)
        self.head = node
        if self.tail is None:
            self.tail = node
        self.size += 1
        return node

    def append(self: LinkedList, value: object) -> Node:
        node = Node(value)
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1
        return node
if __name__ == '__main__':
    try:
        playlist = LinkedList()
        playlist.append('Dawn')
        playlist.append('Harbor')
        print(values(playlist.head), playlist.tail.value)
    except NotImplementedError as error:
        print(error)
