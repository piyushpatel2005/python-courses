from solution import *



def test_01_step():
    "Raise `IndexError` when `dequeue` receives an empty queue."
    q = LinkedQueue()
    try: q.dequeue()
    except IndexError: pass
    else: assert False, "Raise IndexError on empty removal"
    assert q.head is None and q.tail is None and q.size == 0


def test_02_step():
    "Remove and detach the head of a queue with multiple nodes, returning its value and reducing size."
    q = LinkedQueue()
    for x in ["front", "middle", "rear"]: q.enqueue(x)
    old, tail = q.head, q.tail
    assert q.dequeue() == "front"
    assert q.head.value == "middle" and q.tail is tail
    assert old.next is None and q.size == 2


def test_03_complete_behavior():
    "Clear tail when removal empties the queue."
    q = LinkedQueue()
    for value in [None, 8, 8]: q.enqueue(value)
    old = q.head
    assert q.dequeue() is None and old.next is None
    assert q.size == 2 and q.head.value == 8
    assert q.dequeue() == 8 and q.dequeue() == 8
    assert q.head is None and q.tail is None and q.size == 0
    try:
        q.dequeue()
    except IndexError:
        pass
    else:
        assert False, "An empty queue must raise IndexError"
    assert q.size == 0 and q.tail is None
    q.enqueue("again")
    assert q.head is q.tail and q.dequeue() == "again"
