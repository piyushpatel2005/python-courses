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
        raise NotImplementedError('Complete LinkedList.prepend')
if __name__ == '__main__':
    try:
        playlist = LinkedList()
        playlist.prepend('Harbor')
        playlist.prepend('Dawn')
        print(values(playlist.head), playlist.size)
    except NotImplementedError as error:
        print(error)
