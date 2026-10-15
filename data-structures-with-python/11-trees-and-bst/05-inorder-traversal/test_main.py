from solution import *

def test_01_checkpoint():
    'In `visit_inorder`, visit this node and its two subtrees in inorder order.'
    root=Node(8,Node(3,Node(1),Node(6)),Node(11))
    left=root.left
    out=[99]
    visit_inorder(root,out)
    assert out==[99]+[1, 3, 6, 8, 11]
    assert root.left is left and root.left.right.value==6
    visit_inorder(None,out)
    assert out==[99]+[1, 3, 6, 8, 11]
    out=[]
    visit_inorder(Node(2,Node(2),Node(2)),out)
    assert out==[2,2,2]

def test_02_checkpoint():
    'In `inorder`, return a fresh result list populated by the supplied visitor call.'
    a=inorder(None)
    assert a==[] and a is not inorder(None)
    root=Node(8,Node(3,Node(1),Node(6)),Node(11))
    assert inorder(root)==[1, 3, 6, 8, 11]
    a=inorder(root)
    a.clear()
    assert inorder(root)==[1, 3, 6, 8, 11]

