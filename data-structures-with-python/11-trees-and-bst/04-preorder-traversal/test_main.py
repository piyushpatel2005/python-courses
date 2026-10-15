from solution import *

def test_01_checkpoint():
    'In `visit_preorder`, visit this node and its two subtrees in preorder order.'
    root=Node(8,Node(3,Node(1),Node(6)),Node(11))
    left=root.left
    out=[99]
    visit_preorder(root,out)
    assert out==[99]+[8, 3, 1, 6, 11]
    assert root.left is left and root.left.right.value==6
    visit_preorder(None,out)
    assert out==[99]+[8, 3, 1, 6, 11]
    out=[]
    visit_preorder(Node(2,Node(2),Node(2)),out)
    assert out==[2,2,2]

def test_02_checkpoint():
    'In `preorder`, return a fresh result list populated by the supplied visitor call.'
    a=preorder(None)
    assert a==[] and a is not preorder(None)
    root=Node(8,Node(3,Node(1),Node(6)),Node(11))
    assert preorder(root)==[8, 3, 1, 6, 11]
    a=preorder(root)
    a.clear()
    assert preorder(root)==[8, 3, 1, 6, 11]

