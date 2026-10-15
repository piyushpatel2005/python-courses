from solution import *

def test_01_checkpoint():
    'In `within_bounds`, check one key against optional strict lower and upper bounds.'
    assert within_bounds(5,None,None) is True
    assert within_bounds(5,2,8) is True
    assert within_bounds(2,2,8) is False
    assert within_bounds(8,2,8) is False
    assert within_bounds(10**60,None,10**70) is True
    assert within_bounds(-10**60,-10**70,None) is True

def test_02_checkpoint():
    'In `valid_subtree`, validate every subtree using inherited bounds and the single-key check.'
    assert is_bst(None) is True and is_bst(Node(0)) is True
    assert is_bst(Node(10, Node(4, right=Node(12)), Node(16))) is False
    assert is_bst(Node(10, Node(4), Node(16, Node(9)))) is False
    assert is_bst(Node(10, Node(10))) is False
    assert is_bst(Node(10, Node(4, right=Node(10)))) is False
    assert is_bst(Node(10**40, Node(-10**50), Node(10**60))) is True
    tree = BST()
    for value in [9, 2, 15, 1, 5, 12, 18]:
        tree.insert(value)
        assert is_bst(tree.root)
    for value in [9, 1, 15, 5, 2, 12, 18]:
        assert tree.delete(value) and is_bst(tree.root)

