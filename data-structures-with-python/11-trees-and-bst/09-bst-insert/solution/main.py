from __future__ import annotations

from typing import Any, Callable, Iterable

from collections import deque

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
    result: list[int] = []
    visit_preorder(root, result)
    return result

def inorder(root: Node | None) -> list[int]:
    result: list[int] = []
    visit_inorder(root, result)
    return result

def postorder(root: Node | None) -> list[int]:
    result: list[int] = []
    visit_postorder(root, result)
    return result

def level_order(root: Node | None) -> list[int]:
    if root is None:
        return []
    result: list[int] = []
    pending = deque([root])
    while pending:
        node = pending.popleft()
        result.append(node.value)
        enqueue_children(node, pending)
    return result

class BST:

    def __init__(self, root: Node | None=None) -> None:
        self.root: Node | None = root

    def contains(self, value: int) -> bool:
        node = self.root
        while node is not None:
            if value == node.value:
                return True
            node = next_branch(node, value)
        return False

    def insert(self, value: int) -> bool:
        if self.root is None:
            self.root: Node | None = Node(value)
            return True
        node = self.root
        while True:
            if value == node.value:
                return False
            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                    return True
                node = node.left
            else:
                if node.right is None:
                    node.right = Node(value)
                    return True
                node = node.right

def visit_preorder(node: Node | None, result: list[int]) -> None:
    if node is None:
        return
    result.append(node.value)
    visit_preorder(node.left, result)
    visit_preorder(node.right, result)

def visit_inorder(node: Node | None, result: list[int]) -> None:
    if node is None:
        return
    visit_inorder(node.left, result)
    result.append(node.value)
    visit_inorder(node.right, result)

def visit_postorder(node: Node | None, result: list[int]) -> None:
    if node is None:
        return
    visit_postorder(node.left, result)
    visit_postorder(node.right, result)
    result.append(node.value)

def enqueue_children(node: Node, pending: deque[Node]) -> None:
    if node.left is not None:
        pending.append(node.left)
    if node.right is not None:
        pending.append(node.right)

def next_branch(node: Node, value: int) -> Node | None:
    return node.left if value < node.value else node.right

if __name__ == "__main__":
    try:
        tree = BST()
        for value in [12, 5, 18, 7]:
            tree.insert(value)
        print(inorder(tree.root))
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
