from solution import *

def test_01_checkpoint():
    'In `Node.__init__`, store the supplied integer value on the new node.'
    assert Node(12).value==12
    assert Node(-4).value==-4

def test_02_checkpoint():
    'In `Node.__init__`, store the exact left and right child references, including missing children.'
    left,right=Node(3),Node(9)
    root=Node(7,left,right)
    assert root.left is left and root.right is right
    assert left.left is None and left.right is None
    other=Node(1)
    left.left=Node(2)
    assert other.left is None and other.right is None

