from solution import *

def test_01_checkpoint():
    'In `visit_postorder`, visit this node and its two subtrees in postorder order.'
    root=Node(8,Node(3,Node(1),Node(6)),Node(11))
    left=root.left
    out=[99]
    visit_postorder(root,out)
    assert out==[99]+[1, 6, 3, 11, 8]
    assert root.left is left and root.left.right.value==6
    visit_postorder(None,out)
    assert out==[99]+[1, 6, 3, 11, 8]
    out=[]
    visit_postorder(Node(2,Node(2),Node(2)),out)
    assert out==[2,2,2]

def test_02_checkpoint():
    'In `postorder`, return a fresh result list populated by the supplied visitor call.'
    a=postorder(None)
    assert a==[] and a is not postorder(None)
    root=Node(8,Node(3,Node(1),Node(6)),Node(11))
    assert postorder(root)==[1, 6, 3, 11, 8]
    a=postorder(root)
    a.clear()
    assert postorder(root)==[1, 6, 3, 11, 8]

