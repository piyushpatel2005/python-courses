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
        self.head: Node | None  # TODO: assign the empty endpoint
        self.tail: Node | None  # TODO: assign the empty endpoint
        self.size: int = -1  # TODO: assign the empty count
if __name__ == '__main__':
    try:
        playlist = LinkedList()
        print(getattr(playlist, 'head', 'unfinished'), getattr(playlist, 'tail', 'unfinished'), playlist.size)
    except NotImplementedError as error:
        print(error)
