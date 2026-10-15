from solution import *

def check_chain(chain, expected, doubly=False, circular=False):
    assert chain.size == len(expected), "size must count reachable nodes"
    if not expected:
        assert chain.head is None and chain.tail is None
        return []
    nodes=[]
    current=chain.head
    previous=None
    for value in expected:
        assert current is not None and current not in nodes, "broken link or early cycle"
        assert current.value == value
        if doubly:
            assert current.prev is previous, "backward link must mirror forward link"
        nodes.append(current)
        previous,current=current,current.next
    assert chain.tail is nodes[-1], "tail must be the last reachable node"
    assert current is (chain.head if circular else None)
    if doubly:
        assert chain.head.prev is None
        current=chain.tail
        for node in reversed(nodes):
            assert current is node
            current=current.prev
        assert current is None
    return nodes

def expect_error(kind, action):
    try:
        action()
    except kind:
        return
    assert False, "Expected " + kind.__name__

def test_pop_lifo_and_underflow():
    x=Stack(); y=Stack(); expect_error(IndexError,x.pop)
    payload=[]
    for v in [None,0,payload,0]: x.push(v)
    assert x.pop()==0 and x.pop() is payload
    assert x.pop()==0 and x.pop() is None and len(x)==0
    expect_error(IndexError,x.pop); assert x.items==[] and y.items==[]
    x.push("again"); assert x.peek()=="again" and x.pop()=="again"
