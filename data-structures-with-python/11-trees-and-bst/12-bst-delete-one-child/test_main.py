from solution import *

def test_01_checkpoint():
    'In `BST.delete_one_child`, return false when the search finds no node.'
    assert BST().delete_one_child(4) is False
    t=BST(Node(8))
    assert t.delete_one_child(99) is False and t.root.value==8

def test_02_checkpoint():
    'In `BST.delete_one_child`, delegate a leaf to the completed leaf-deletion method.'
    t=BST(Node(4))
    assert t.delete_one_child(4) is True and t.root is None

def test_03_checkpoint():
    'In `BST.delete_one_child`, reject a node with two children without changing its links.'
    t=BST(Node(8,Node(3),Node(11)))
    assert t.delete_one_child(8) is False and inorder(t.root)==[3,8,11]

def test_04_checkpoint():
    "In `BST.delete_one_child`, promote the existing child into the removed node's incoming link."
    for root in (Node(8,Node(3,Node(1))),Node(8,right=Node(11,right=Node(14)))):
        t=BST(root)
        child=root.left if root.left is not None else root.right
        try: t.delete_one_child(8)
        except NotImplementedError: pass
        assert t.root is child and count_nodes(t.root)==2
    t=BST(Node(8,Node(3,right=Node(6)),Node(11)))
    child=t.root.left.right
    try: t.delete_one_child(3)
    except NotImplementedError: pass
    assert t.root.left is child

def test_05_checkpoint():
    "In `BST.delete_one_child`, detach the removed node's links and return success."
    for root in [Node(8, Node(3, Node(1))), Node(8, right=Node(11, right=Node(14)))]:
        tree = BST(root)
        child = root.left if root.left is not None else root.right
        assert tree.delete_one_child(8) is True and tree.root is child
        assert root.left is None and root.right is None
        assert count_nodes(tree.root) == 2
    tree = BST(Node(8, Node(3, right=Node(6)), Node(11)))
    old, child = tree.root.left, tree.root.left.right
    assert tree.delete_one_child(3) is True and tree.root.left is child
    assert old.left is None and old.right is None
    assert tree.delete_one_child(8) is False
    assert tree.delete_one_child(11) is True
    assert tree.delete_one_child(99) is False
    assert inorder(tree.root) == [6, 8]

