from solution import *



def test_01_step():
    "Raise `OverflowError` for a full ring without changing it."
    q = RingQueue(2)
    q.data[:] = ["a", "b"]; q.size = 2
    try: q.enqueue("c")
    except OverflowError: pass
    else: assert False, "Reject a full ring"
    assert q.data == ["a", "b"] and q.size == 2 and q.head == 0


def test_02_step():
    "Write the value into the wrapped rear slot without moving head."
    q = RingQueue(3)
    q.head, q.size = 2, 1
    q.data[2] = "old"
    original = q.data
    q.enqueue("new")
    assert q.data is original and q.data == ["new", None, "old"] and q.head == 2


def test_03_complete_behavior():
    "Increase size after a successful write."
    q = RingQueue(3)
    q.head = 2
    q.data[2] = "old"
    q.size = 1
    storage = q.data
    assert q.enqueue(None) is None
    q.enqueue("new")
    assert q.data is storage and q.data == [None, "new", "old"]
    assert q.head == 2 and q.size == 3
    saved = q.data[:]
    try:
        q.enqueue("overflow")
    except OverflowError:
        pass
    else:
        assert False, "A full ring must reject insertion"
    assert q.data == saved and q.size == 3 and len(q.data) == 3
    one = RingQueue(1)
    one.enqueue(0)
    assert one.data == [0] and one.size == 1
