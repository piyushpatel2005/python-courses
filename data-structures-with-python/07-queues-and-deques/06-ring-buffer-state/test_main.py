from solution import *



def test_01_step():
    "Reject an invalid capacity with `ValueError`."
    for bad in [0, -1, True, 2.5, "3"]:
        try: RingQueue(bad)
        except ValueError: pass
        else: assert False, "Reject invalid capacity"
    RingQueue(1)


def test_02_step():
    "Allocate an independent `data` list containing capacity empty slots."
    a, b = RingQueue(3), RingQueue(3)
    assert a.data == [None, None, None]
    a.data[0] = "used"
    assert b.data == [None, None, None]


def test_03_complete_behavior():
    "Initialize `head` and `size` to zero."
    for capacity in [1, 3, 9]:
        a, b = RingQueue(capacity), RingQueue(capacity)
        assert a.data == [None] * capacity and a.head == 0 and a.size == 0
        a.data[0] = "changed"
        assert b.data[0] is None
    for bad in [0, -2, 1.5, True, "3"]:
        try:
            RingQueue(bad)
        except ValueError:
            pass
        else:
            assert False, "Capacity must be a positive integer, not bool"
