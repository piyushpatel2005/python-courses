from solution import *

def test_01_checkpoint():
    'In `BST.minimum`, return `None` when the tree has no minimum.'
    assert BST().minimum() is None

def test_02_checkpoint():
    'In `BST.minimum`, read the leftmost key without changing any link.'
    for root,expected in ((Node(0),0),(Node(8,Node(3,Node(-2)),Node(11)),-2),(Node(2,right=Node(5)),2)):
        t=BST(root)
        before=inorder(root)
        assert t.minimum()==expected and t.root is root and inorder(root)==before

