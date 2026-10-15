from solution import *

def test_push_appends_references():
    x=Stack(); y=Stack(); payload=[]
    assert x.push(payload) is None
    assert x.items[0] is payload
    x.push(0); x.push(0); x.push(None)
    assert x.items==[[],0,0,None] and len(x)==4
    payload.append(9); assert x.items[0]==[9]
    assert y.items==[]
