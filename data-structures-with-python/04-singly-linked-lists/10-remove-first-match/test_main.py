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

def test_remove_first_duplicate_policy():
    x=LinkedList(); assert x.remove_first(2) is None
    nodes=[x.append(v) for v in [1,2,2,3]]
    removed=x.remove_first(2)
    assert removed is nodes[1] and removed.next is None
    assert check_chain(x,[1,2,3]) == [nodes[0],nodes[2],nodes[3]]
    assert x.remove_first(9) is None; check_chain(x,[1,2,3])
    assert x.remove_first(1) is nodes[0]; check_chain(x,[2,3])
    assert x.remove_first(3) is nodes[3]; check_chain(x,[2])
    assert x.remove_first(2) is nodes[2]; check_chain(x,[])
    n=x.append(None); assert x.remove_first(None) is n; check_chain(x,[])
