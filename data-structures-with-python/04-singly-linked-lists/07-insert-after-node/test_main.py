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

def test_insert_after_splices():
    x=LinkedList()
    expect_error(ValueError,lambda:x.insert_after(None,8)); check_chain(x,[])
    a=x.append(1); c=x.append(3)
    b=x.insert_after(a,2); d=x.insert_after(c,4)
    assert check_chain(x,[1,2,3,4]) == [a,b,c,d]
    e=x.insert_after(d,4)
    assert check_chain(x,[1,2,3,4,4]) == [a,b,c,d,e]
    expect_error(ValueError,lambda:x.insert_after(None,9))
    check_chain(x,[1,2,3,4,4])
