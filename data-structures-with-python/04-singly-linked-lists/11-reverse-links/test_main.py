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

def test_reverse_preserves_node_identity():
    x=LinkedList(); assert x.reverse() is None; check_chain(x,[])
    one=x.append(7); x.reverse(); assert check_chain(x,[7]) == [one]
    nodes=[one,x.append(2),x.append(7),x.append(None)]
    assert x.reverse() is None
    assert check_chain(x,[None,7,2,7]) == nodes[::-1]
    x.reverse(); assert check_chain(x,[7,2,7,None]) == nodes
    assert [n.value for n in nodes] == [7,2,7,None]
