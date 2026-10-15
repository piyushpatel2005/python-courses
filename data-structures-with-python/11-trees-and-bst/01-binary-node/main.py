from __future__ import annotations

from typing import Any, Callable, Iterable

class Node:

    def __init__(self, value: int, left: Node | None=None, right: Node | None=None) -> None:
        # TODO task 1: In `Node.__init__`, store the supplied integer value on the new node.
        pass
        # TODO task 2: In `Node.__init__`, store the exact left and right child references, including missing children.
        pass

if __name__ == "__main__":
    try:
        root = Node(12, Node(5), Node(18))
        print(root.value, root.left.value, root.right.value)
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
