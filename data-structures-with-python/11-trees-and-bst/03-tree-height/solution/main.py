from __future__ import annotations

from typing import Any, Callable, Iterable

class Node:

    def __init__(self, value: int, left: Node | None=None, right: Node | None=None) -> None:
        self.value: int = value
        self.left: Node | None = left
        self.right: Node | None = right

def count_nodes(root: Node | None) -> int:
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def height(root: Node | None) -> int:
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

if __name__ == "__main__":
    try:
        root = Node(12, Node(5, Node(2)), Node(18))
        print(height(root))
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
