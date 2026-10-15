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

def test_skip_height_validation():
    for bad in [0,-1,1.5,True]:
        expect_error(ValueError,lambda bad=bad:SkipNode(1,bad))


def test_skip_node_slots():
    a=SkipNode(12,3); b=SkipNode(17,3)
    assert a.key == 12 and a.forward == [None,None,None]
    assert a.forward is not b.forward
    a.forward[0]=b
    assert b.forward == [None,None,None]
    assert SkipNode(0,1).forward == [None]
    x=SkipList(3)
    assert x.head.key is None and x.head.forward == [None]*3
    assert x.tail is None and x.size == 0
