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

def test_remove_head_detaches():
    x=LinkedList(); expect_error(IndexError,x.remove_head); check_chain(x,[])
    a=x.append(2); b=x.append(2)
    assert x.remove_head() is a and a.next is None
    check_chain(x,[2])
    assert x.remove_head() is b and b.next is None
    check_chain(x,[]); expect_error(IndexError,x.remove_head)
    c=x.append(None); assert check_chain(x,[None]) == [c]
