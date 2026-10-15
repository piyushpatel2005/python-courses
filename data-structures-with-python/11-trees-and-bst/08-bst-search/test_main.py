from solution import *

def test_01_checkpoint():
    'In `next_branch`, choose the existing child that could contain a different search key.'
    left,right=Node(2),Node(9)
    root=Node(5,left,right)
    assert next_branch(root,3) is left
    assert next_branch(root,8) is right
    assert next_branch(left,1) is None
    assert root.left is left and root.right is right

def test_02_checkpoint():
    'In `BST.contains`, follow one search branch until a match or missing child, without changing the root.'
    assert BST().contains(1) is False
    tree = BST(Node(8, Node(3, Node(1), Node(6)), Node(11)))
    root = tree.root
    for value in [1, 3, 6, 8, 11]: assert tree.contains(value) is True
    for value in [-1, 2, 7, 12]: assert tree.contains(value) is False
    assert tree.root is root and inorder(tree.root) == [1, 3, 6, 8, 11]

