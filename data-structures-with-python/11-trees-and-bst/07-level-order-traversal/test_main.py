from solution import *

def test_01_checkpoint():
    'In `enqueue_children`, append existing children left first without disturbing the pending queue.'
    old,left,right=Node(99),Node(3),Node(8)
    q=deque([old])
    enqueue_children(Node(5,left,right),q)
    assert list(q)==[old,left,right]
    enqueue_children(Node(2),q)
    assert list(q)==[old,left,right]
    q=deque()
    enqueue_children(Node(1,right=right),q)
    assert list(q)==[right]

def test_02_checkpoint():
    'In `level_order`, process pending nodes in FIFO order, recording each value and queuing its children.'
    assert level_order(None) == [] and level_order(Node(2)) == [2]
    root = Node(8, Node(3, Node(1), Node(6)), Node(11, right=Node(14)))
    left = root.left
    assert level_order(root) == [8, 3, 11, 1, 6, 14]
    assert root.left is left and root.right.right.value == 14
    assert level_order(Node(2, Node(2), Node(2))) == [2, 2, 2]

