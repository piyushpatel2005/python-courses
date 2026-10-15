from solution import *

def test_01_checkpoint():
    'In `Scheduler.has_due`, check whether the earliest live job is due, without removing that job.'
    s=Scheduler()
    assert s.has_due(0) is False
    s.schedule('a',3)
    s.schedule('a',8)
    s.schedule('b',5)
    assert s.has_due(4) is False and s.has_due(5) is True
    assert s.queue.peek()==('b',5)
    assert s.has_due(5) is True

def test_02_checkpoint():
    'In `Scheduler.run_due`, drain ready jobs through `now`, stopping before the first future job.'
    s = Scheduler()
    assert s.run_due(0) == []
    s.schedule('a', 3)
    s.schedule('b', 3)
    s.schedule('c', 9)
    s.schedule('a', 8)
    assert s.run_due(3) == ['b']
    assert s.run_due(3) == [] and s.queue.peek() == ('a', 8)
    s.schedule('c', 8)
    assert s.run_due(7) == []
    assert s.run_due(8) == ['a', 'c']
    assert s.run_due(100) == []
    s.schedule('b', -2)
    assert s.run_due(-2) == ['b']
    other = Scheduler()
    other.schedule('x', 1)
    assert other.run_due(1) == ['x'] and s.run_due(1) == []

