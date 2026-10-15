from solution import *



def test_01_step():
    "Set `head` and `tail` on the new queue to `None`."
    a, b = LinkedQueue(), LinkedQueue()
    assert a.head is None and a.tail is None
    assert b.head is None and b.tail is None
    a.head = Node("owned")
    assert b.head is None


def test_02_complete_behavior():
    "Set the new queue's `size` to zero."
    a, b = LinkedQueue(), LinkedQueue()
    assert a.head is None and a.tail is None and a.size == 0
    assert b.head is None and b.tail is None and b.size == 0
    a.head = Node("private")
    a.size = 1
    assert b.head is None and b.size == 0
