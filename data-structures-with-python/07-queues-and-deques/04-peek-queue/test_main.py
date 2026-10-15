from solution import *



def test_01_step():
    "Raise `IndexError` when `peek` receives an empty queue."
    q = LinkedQueue()
    try: q.peek()
    except IndexError: pass
    else: assert False, "Raise IndexError when empty"
    assert q.size == 0


def test_02_complete_behavior():
    "Return the head value without changing a nonempty queue."
    q = LinkedQueue()
    try:
        q.peek()
    except IndexError:
        pass
    else:
        assert False, "An empty peek must raise IndexError"
    for value in [None, 0, "tail"]: q.enqueue(value)
    a, b, link = q.head, q.tail, q.head.next
    assert q.peek() is None and q.peek() is None
    assert q.head is a and q.tail is b and q.head.next is link and q.size == 3
    assert q.dequeue() is None and q.peek() == 0
