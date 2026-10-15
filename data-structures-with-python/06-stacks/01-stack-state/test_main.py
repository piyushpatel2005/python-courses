from solution import *

def test_stack_independent_storage():
    a=Stack(); b=Stack()
    assert a.items==[] and b.items==[] and len(a)==0
    assert a.items is not b.items
    a.items.append(3)
    assert len(a)==1 and b.items==[] and len(b)==0
