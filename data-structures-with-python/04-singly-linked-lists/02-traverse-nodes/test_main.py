from solution import *

def test_values_walk():
    assert values(None) == []
    payload=[]
    c=Node(payload); b=Node(0,c); a=Node(None,b)
    result=values(a)
    assert result == [None,0,[]] and result[2] is payload
    assert a.next is b and b.next is c and c.next is None
    result.clear()
    assert values(a) == [None,0,[]]
    assert values(Node("solo")) == ["solo"]
