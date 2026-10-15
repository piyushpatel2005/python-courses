from solution import *

def test_01_checkpoint():
    'In `successor_of`, locate the leftmost node of the right subtree together with its parent.'
    r=Node(8,Node(3),Node(15,Node(11,right=Node(12)),Node(18)))
    p,s=successor_of(r)
    assert p is r.right and s is r.right.left and s.right.value==12
    r=Node(8,Node(3),Node(11))
    p,s=successor_of(r)
    assert p is r and s is r.right

def test_02_checkpoint():
    'In `BST.delete`, return false when no matching node exists.'
    assert BST().delete(1) is False
    t=BST(Node(2))
    assert t.delete(1) is False and t.root.value==2

def test_03_checkpoint():
    'In `BST.delete`, delegate a target with fewer than two children to the completed deletion method.'
    root=Node(8,right=Node(11))
    t=BST(root)
    child=root.right
    assert t.delete(8) is True and t.root is child
    assert t.delete(11) is True and t.root is None

def test_04_checkpoint():
    'In `BST.delete`, copy the successor key, splice its right child upward, and detach the successor.'
    for values in [[8, 3, 11], [8, 3, 15, 11, 18, 12], [8, 3, 15, 1, 6, 4, 7]]:
        tree = BST()
        for value in values: tree.insert(value)
        root = tree.root
        successor = root.right
        while successor.left is not None: successor = successor.left
        expected_key = successor.value
        assert tree.delete(8) is True
        assert tree.root is root and root.value == expected_key
        assert successor.left is None and successor.right is None
        assert inorder(tree.root) == sorted(set(values) - {8})
        for value in values:
            if value != 8: assert tree.delete(value) is True
        assert tree.root is None and tree.delete(99) is False
    tree = BST()
    for x in [20, 10, 30, 5, 15, 12, 17]: tree.insert(x)
    assert tree.delete(10) is True and inorder(tree.root) == [5, 12, 15, 17, 20, 30]

