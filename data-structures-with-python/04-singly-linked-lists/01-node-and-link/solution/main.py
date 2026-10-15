from __future__ import annotations

class Node:

    def __init__(self: Node, value: object, next_node: Node | None=None) -> None:
        self.value: object = value
        self.next: Node | None = next_node
if __name__ == '__main__':
    try:
        end = Node('Harbor')
        start = Node('Dawn', end)
        print(start.value, start.next.value if start.next is not None else None, end.next)
    except NotImplementedError as error:
        print(error)
