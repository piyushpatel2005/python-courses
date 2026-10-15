from solution import *

def test_01_checkpoint():
    'In `count_nodes`, return zero for a missing subtree.'
    assert count_nodes(None)==0

def test_02_checkpoint():
    'In `count_nodes`, combine both recursive child counts with the current node.'
    assert count_nodes(None) == 0
    leaf = Node(0)
    assert count_nodes(leaf) == 1
    root = Node(3, Node(3, Node(-1)), Node(3))
    left, right = root.left, root.right
    assert count_nodes(root) == 4 and count_nodes(root) == 4
    assert root.left is left and root.right is right and root.left.left.value == -1
    assert count_nodes(Node(9, right=Node(8, right=Node(7)))) == 3

