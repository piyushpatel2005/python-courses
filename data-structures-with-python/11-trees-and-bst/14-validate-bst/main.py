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

    def minimum(self) -> int | None:
        if self.root is None:
            return None
        node = self.root
        while node.left is not None:
            node = node.left
        return node.value

    def _locate(self, value: int) -> tuple[Node | None, Node | None]:
        parent = None
        node = self.root
        while node is not None and node.value != value:
            parent = node
            node = node.left if value < node.value else node.right
        return (parent, node)

    def _replace(self, parent: Node | None, node: Node | None, replacement: Node | None) -> None:
        if parent is None:
            self.root: Node | None = replacement
        elif parent.left is node:
            parent.left = replacement
        else:
            parent.right = replacement

    def delete_leaf(self, value: int) -> bool:
        parent, node = self._locate(value)
        if node is None or node.left is not None or node.right is not None:
            return False
        self._replace(parent, node, None)
        return True

    def delete_one_child(self, value: int) -> bool:
        parent, node = self._locate(value)
        if node is None:
            return False
        if node.left is None and node.right is None:
            return self.delete_leaf(value)
        if node.left is not None and node.right is not None:
            return False
        child = node.left if node.left is not None else node.right
        self._replace(parent, node, child)
        node.left = None
        node.right = None
        return True

    def delete(self, value: int) -> bool:
        parent, node = self._locate(value)
        if node is None:
            return False
        if node.left is None or node.right is None:
            return self.delete_one_child(value)
        successor_parent, successor = successor_of(node)
        node.value = successor.value
        self._replace(successor_parent, successor, successor.right)
        successor.left = None
        successor.right = None
        return True

def is_bst(root: Node | None) -> bool:
    return valid_subtree(root, None, None)

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

def successor_of(node: Node) -> tuple[Node, Node]:
    parent = node
    successor = node.right
    while successor.left is not None:
        parent = successor
        successor = successor.left
    return (parent, successor)

def within_bounds(value: int, lower: int | None, upper: int | None) -> bool:
    # TODO task 1: In `within_bounds`, check one key against optional strict lower and upper bounds.
    raise NotImplementedError('Complete this step')

def valid_subtree(node: Node | None, lower: int | None, upper: int | None) -> bool:
    # TODO task 2: In `valid_subtree`, validate every subtree using inherited bounds and the single-key check.
    raise NotImplementedError('Complete this step')

if __name__ == "__main__":
    try:
        print(is_bst(Node(12, Node(5, right=Node(14)), Node(18))))
    except (NotImplementedError, AttributeError, TypeError) as error:
        print("Unfinished checkpoint:", error)
