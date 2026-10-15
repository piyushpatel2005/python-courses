from solution import *

def test_01_checkpoint():
    'In `height`, give a missing subtree height zero.'
    assert height(None)==0

def test_02_checkpoint():
    'In `height`, return one plus the larger recursive child height.'
    assert height(Node(4))==1
    assert height(Node(1,Node(2),Node(3)))==2
    chain=Node(1,right=Node(2,right=Node(3,right=Node(4))))
    assert height(chain)==4 and count_nodes(chain)==4

