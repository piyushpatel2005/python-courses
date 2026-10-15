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

def test_visit_replaces_forward_branch():
    h=BrowserHistory("A"); other=BrowserHistory("Other")
    assert h.visit("B")=="B"; old_b=h.current
    h.visit("C"); old_c=h.current
    assert h.back()=="B" and h.back()=="A" and h.back()=="A"
    assert h.visit("D")=="D"
    check_chain(h.pages,["A","D"],True)
    assert h.current is h.pages.tail and h.forward()=="D"
    assert old_b.prev is None and old_b.next is None
    assert old_c.prev is None and old_c.next is None
    h.visit("D"); check_chain(h.pages,["A","D","D"],True)
    assert h.back()=="D" and h.forward()=="D"
    check_chain(other.pages,["Other"],True)
