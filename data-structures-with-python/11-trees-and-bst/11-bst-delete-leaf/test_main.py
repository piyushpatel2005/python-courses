from solution import *

def test_01_checkpoint():
    'In `BST.delete_leaf`, reject a missing key or a node with any child.'
    t=BST(Node(8,Node(3),Node(11)))
    root=t.root
    assert t.delete_leaf(8) is False and t.delete_leaf(99) is False
    assert t.root is root and inorder(root)==[3,8,11]
    assert BST().delete_leaf(0) is False

def test_02_checkpoint():
    'In `BST.delete_leaf`, disconnect the found leaf and report successful removal.'
    t=BST(Node(8,Node(3),Node(11)))
    root=t.root
    assert t.delete_leaf(3) is True and root.left is None
    assert root.right.value==11 and t.root is root
    single=BST(Node(0))
    assert single.delete_leaf(0) is True and single.root is None

