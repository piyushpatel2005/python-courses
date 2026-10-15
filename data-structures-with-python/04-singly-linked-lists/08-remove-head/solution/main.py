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

    def find(self: LinkedList, value: object) -> Node | None:
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def insert_after(self: LinkedList, previous: Node | None, value: object) -> Node:
        if previous is None:
            raise ValueError('A live predecessor is required')
        node = Node(value, previous.next)
        previous.next = node
        if self.tail is previous:
            self.tail = node
        self.size += 1
        return node

    def remove_head(self: LinkedList) -> Node:
        if self.head is None:
            raise IndexError('Empty list')
        removed = self.head
        self.head = removed.next
        self.size -= 1
        if self.head is None:
            self.tail = None
        removed.next = None
        return removed
if __name__ == '__main__':
    try:
        playlist = LinkedList()
        playlist.append('Dawn')
        playlist.append('Harbor')
        played = playlist.remove_head()
        print(played.value, values(playlist.head), played.next)
    except NotImplementedError as error:
        print(error)
