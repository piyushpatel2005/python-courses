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

def test_find_first_match_without_changing_missing_ring():
    x = CircularList()
    assert x.remove_first('absent') is None
    nodes = [x.append(v) for v in [4, 5, 4]]
    assert x.remove_first(99) is None
    assert check_chain(x, [4, 5, 4], circular=True) == nodes
    assert x.remove_first(4) is nodes[0], 'Find the first head-first match'


def test_splice_and_repair_endpoints():
    x = CircularList()
    a, b, c = [x.append(v) for v in [4, 5, 6]]
    assert x.remove_first(4) is a
    assert x.head is b and x.tail is c and b.next is c and c.next is b
    x = CircularList()
    a, b, c = [x.append(v) for v in [4, 5, 6]]
    assert x.remove_first(5) is b
    assert a.next is c and c.next is a and x.head is a and x.tail is c
    x = CircularList()
    only = x.append(4)
    assert x.remove_first(4) is only
    assert x.head is None and x.tail is None
    x = CircularList()
    a, b = [x.append(v) for v in [4, 5]]
    assert x.remove_first(5) is b
    assert x.head is a and x.tail is a and a.next is a


def test_detach_count_and_full_operation():
    x = CircularList()
    nodes = [x.append(v) for v in [4, 5, 4, 6]]
    assert x.remove_first(4) is nodes[0] and nodes[0].next is None
    assert check_chain(x, [5, 4, 6], circular=True) == nodes[1:]
    assert x.remove_first(99) is None
    check_chain(x, [5, 4, 6], circular=True)
    assert x.remove_first(6) is nodes[3] and nodes[3].next is None
    check_chain(x, [5, 4], circular=True)
    assert x.remove_first(4) is nodes[2] and nodes[2].next is None
    check_chain(x, [5], circular=True)
    assert x.remove_first(5) is nodes[1] and nodes[1].next is None
    check_chain(x, [], circular=True)
    x.append(0); middle = x.append(7); x.append(9)
    assert x.remove_first(7) is middle and middle.next is None
    check_chain(x, [0, 9], circular=True)
