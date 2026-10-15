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

def test_double_remove_repairs_neighbors():
    x=DoublyList(); expect_error(ValueError,lambda:x.remove(None))
    nodes=[x.append(v) for v in [2,2,3]]
    assert x.remove(nodes[1]) is nodes[1]
    assert nodes[1].prev is None and nodes[1].next is None
    assert check_chain(x,[2,3],True)==[nodes[0],nodes[2]]
    x.remove(nodes[0]); check_chain(x,[3],True)
    assert nodes[0].next is None and nodes[0].prev is None
    x.remove(nodes[2]); check_chain(x,[],True)
    assert nodes[2].next is None and nodes[2].prev is None
    x.append(6); check_chain(x,[6],True)
    tail=x.append(8)
    assert x.remove(tail) is tail
    assert tail.prev is None and tail.next is None
    check_chain(x,[6],True)
