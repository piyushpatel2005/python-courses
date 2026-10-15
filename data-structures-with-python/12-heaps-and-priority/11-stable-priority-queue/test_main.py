from solution import *

def test_01_checkpoint():
    'In `PriorityQueue._take_ticket`, reserve and return a unique increasing ticket for this queue.'
    q,r=PriorityQueue(),PriorityQueue()
    assert [q._take_ticket() for _ in range(4)]==[0,1,2,3]
    assert r._take_ticket()==0
    assert q._counter==4

def test_02_checkpoint():
    'In `PriorityQueue.push`, push a `(priority, ticket, task)` entry using the reserved ticket.'
    q = PriorityQueue()
    a, b, c = {'id': 'a'}, {'id': 'b'}, object()
    q.push(a, 3)
    q.push(b, 3)
    q.push(c, 1)
    assert q.pop() is c and q.pop() is a
    q.push(a, 3)
    assert q.pop() is b and q.pop() is a
    assert q._counter == 4
    other = PriorityQueue()
    other.push(b, -2)
    assert other.pop() is b and not q._heap
    try:
        q.pop()
        assert False
    except IndexError:
        pass

