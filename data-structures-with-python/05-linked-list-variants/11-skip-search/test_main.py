from solution import *

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

def test_skip_search_exact_match():
    x=seed_skip([(2,2),(9,1),(21,3)],4)
    nodes=check_skip(x,[2,9,21])
    for key,node in zip([2,9,21],nodes):
        assert x.search(key) is node
    for key in [-4,3,20,22]:
        assert x.search(key) is None
    assert SkipList().search(2) is None
    check_skip(x,[2,9,21])
    original=x.predecessors; calls=[]
    def observed(key):
        calls.append(key)
        return original(key)
    x.predecessors=observed
    assert x.search(9) is nodes[1] and calls==[9]
