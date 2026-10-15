from solution import *

def test_01_checkpoint():
    'In `BST.insert`, create the root when inserting into an empty tree.'
    a,b=BST(),BST()
    assert a.insert(7) is True and a.root.value==7
    assert a.root.left is None and a.root.right is None and b.root is None

def test_02_checkpoint():
    'In `BST.insert`, reject a duplicate key without changing any links.'
    left=Node(3)
    root=Node(8,left,Node(12))
    t=BST(root)
    assert t.insert(3) is False and t.root is root and root.left is left
    assert count_nodes(root)==3

def test_03_checkpoint():
    'In `BST.insert`, attach a new leaf at a missing left link.'
    t=BST(Node(8,Node(4),Node(12)))
    root=t.root
    assert t.insert(2) is True
    assert root.left.left.value==2 and t.root is root
    assert inorder(root)==[2,4,8,12]

def test_04_checkpoint():
    'In `BST.insert`, attach a new leaf at a missing right link.'
    t=BST(Node(8,Node(4),Node(12)))
    root=t.root
    assert t.insert(6) is True and root.left.right.value==6
    assert t.insert(15) is True and root.right.right.value==15
    assert inorder(root)==[4,6,8,12,15]

