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

def test_play_next_delegates_and_drains():
    x=LinkedList(); assert x.play_next() is None; check_chain(x,[])
    first=x.append("Blue hour"); x.append("Blue hour"); x.append("Orchard")
    original=x.remove_head; calls=[]
    def observed():
        calls.append(True)
        return original()
    x.remove_head=observed
    assert x.play_next() == "Blue hour" and len(calls)==1
    assert first.next is None; check_chain(x,["Blue hour","Orchard"])
    assert x.play_next() == "Blue hour"
    assert x.play_next() == "Orchard"
    assert x.play_next() is None and len(calls)==3; check_chain(x,[])
    x.append("Return"); assert x.play_next()=="Return"; check_chain(x,[])
