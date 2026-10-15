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

def preorder(root: Node | None) -> list[int]:
    # TODO task 2: In `preorder`, return a fresh result list populated by the supplied visitor call.
    raise NotImplementedError('Complete this step')

def visit_preorder(node: Node | None, result: list[int]) -> None:
    # TODO task 1: In `visit_preorder`, visit this node and its two subtrees in preorder order.
    raise NotImplementedError('Complete this step')

if __name__ == "__main__":
    try:
        root = Node(12, Node(5, Node(2)), Node(18))
        print(preorder(root))
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
