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

def check_skip(s, expected):
    assert s.size == len(expected)
    base=[]
    current=s.head.forward[0]
    for key in expected:
        assert current is not None and current not in base
        assert current.key==key
        assert 1 <= len(current.forward) <= s.max_level
        base.append(current)
        current=current.forward[0]
    assert current is None
    assert s.tail is (base[-1] if base else None)
    for level in range(s.max_level):
        actual=[]; current=s.head.forward[level]
        for node in base:
            if len(node.forward)>level:
                assert current is node, "Every tower must occur on each of its levels"
                actual.append(current)
                current=current.forward[level]
        assert current is None, "No extra node or cycle at upper level"
    return base

def test_insert_rejects_height_before_search():
    x=SkipList(4)
    original=x.predecessors
    def forbidden(key):
        raise AssertionError('Validate before searching')
    x.predecessors=forbidden
    try:
        for bad in [0,5,-1,True,2.5]:
            expect_error(ValueError,lambda bad=bad:x.insert(17,bad))
    finally:
        x.predecessors=original
    check_skip(x,[])


def test_insert_preserves_duplicate_tower():
    x=seed_skip([(4,1),(17,3),(29,2)],4)
    nodes=check_skip(x,[4,17,29])
    assert x.insert(17,1) is False
    assert check_skip(x,[4,17,29]) == nodes
    assert len(x.search(17).forward) == 3


def test_skip_insert_towers_and_duplicates():
    x=SkipList(4); other=SkipList(4)
    for key,height in [(17,3),(4,1),(29,2),(11,4),(35,1),(-2,2)]:
        assert x.insert(key,height) is True
        assert len(x.search(key).forward) == height, "Use the supplied height for each new tower"
        check_skip(x,sorted([n for n in [-2,4,11,17,29,35] if x.search(n) is not None]))
    nodes=check_skip(x,[-2,4,11,17,29,35]); old=x.search(17)
    assert len(old.forward)==3 and x.insert(17,1) is False
    assert x.search(17) is old and len(old.forward)==3
    assert check_skip(x,[-2,4,11,17,29,35])==nodes
    for bad in [0,5,True,2.5]:
        expect_error(ValueError,lambda bad=bad:x.insert(17,bad))
        expect_error(ValueError,lambda bad=bad:x.insert(50,bad))
        check_skip(x,[-2,4,11,17,29,35])
    check_skip(other,[])
