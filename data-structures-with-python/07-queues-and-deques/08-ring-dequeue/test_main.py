from solution import *



def test_01_step():
    "Raise `IndexError` for an empty ring without changing it."
    q = RingQueue(3)
    try: q.dequeue()
    except IndexError: pass
    else: assert False, "Reject empty removal"
    assert q.head == 0 and q.size == 0 and q.data == [None] * 3


def test_02_step():
    "Save, clear, and return the value in the head slot."
    q = RingQueue(3)
    q.head, q.size = 2, 1
    q.data[2] = "reading"
    assert q.dequeue() == "reading" and q.data[2] is None


def test_03_complete_behavior():
    "Advance head with wraparound and reduce size after removal."
    q = RingQueue(3)
    model = []
    for i in range(30):
        if len(model) == 3:
            old_head = q.head
            assert q.dequeue() == model.pop(0)
            assert q.data[old_head] is None
        q.enqueue(None if i % 4 == 0 else i)
        model.append(None if i % 4 == 0 else i)
        assert q.size == len(model) and len(q.data) == 3
    while model:
        old_head = q.head
        assert q.dequeue() == model.pop(0)
        assert q.head == (old_head + 1) % 3
    assert q.data == [None] * 3 and q.size == 0
    saved = (q.head, q.size, q.data[:])
    try:
        q.dequeue()
    except IndexError:
        pass
    else:
        assert False, "Empty removal must fail"
    assert (q.head, q.size, q.data) == saved
    q.enqueue("reuse")
    assert q.dequeue() == "reuse"
