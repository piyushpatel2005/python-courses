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

def test_skip_work_metric_and_shape():
    flat=seed_skip([(10,1),(20,1),(30,1),(40,1),(50,1)],3)
    tall=seed_skip([(10,1),(20,2),(30,1),(40,3),(50,1)],3)
    assert flat.search_steps(50)==(True,7)
    assert tall.search_steps(50)==(True,4)
    assert tall.search_steps(41)==(False,4)
    assert tall.search_steps(1)==(False,3)
    assert SkipList(2).search_steps(1)==(False,2)
    for s in [flat,tall]:
        for key in range(0,62,3):
            found,moves=s.search_steps(key)
            assert found is (s.search(key) is not None)
            assert s.max_level <= moves <= s.size+s.max_level
        check_skip(s,[10,20,30,40,50])
