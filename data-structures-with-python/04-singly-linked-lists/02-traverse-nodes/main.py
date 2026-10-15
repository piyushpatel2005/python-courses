from __future__ import annotations

class Node:

    def __init__(self: Node, value: object, next_node: Node | None=None) -> None:
        self.value: object = value
        self.next: Node | None = next_node

def values(head: Node | None) -> list[object]:
    raise NotImplementedError('Complete values')
if __name__ == '__main__':
    try:
        chain = Node('Dawn', Node('Harbor'))
        print(values(chain))
    except NotImplementedError as error:
        print(error)
