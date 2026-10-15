from solution import *

def test_01_checkpoint():
    'In `UpdatingQueue._publish`, publish a fresh active ticket for a task and return that ticket.'
    q=UpdatingQueue()
    assert q._publish('a')==0 and q._active=={'a':0}
    assert q._publish('b')==1
    assert q._publish('a')==2 and q._active=={'a':2,'b':1}
    assert q._heap==[] and q._counter==3

def test_02_checkpoint():
    'In `UpdatingQueue.update`, push the new priority entry while leaving old versions in the heap.'
    q = UpdatingQueue()
    q.update('a', 1)
    q.update('b', 2)
    q.update('a', 5)
    assert len(q._heap) == 3 and q.peek() == ('b', 2)
    assert q.pop() == ('b', 2) and q.pop() == ('a', 5)
    q.update('a', 3)
    q.update('b', 3)
    q.update('a', 3)
    assert q.pop() == ('b', 3) and q.pop() == ('a', 3)
    q.update('x', 9)
    q.update('x', -1)
    assert q.pop() == ('x', -1)
    try:
        q.pop()
        assert False
    except IndexError:
        pass
    assert q._active == {}
    other = UpdatingQueue()
    other.update('z', 0)
    assert other.pop() == ('z', 0)

