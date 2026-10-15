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

def test_locate_exact_candidate_and_reject_missing_key():
    x = seed_skip([(7, 2), (18, 4), (30, 1)], 4)
    nodes = check_skip(x, [7, 18, 30])
    assert x.remove(17) is False
    assert x.remove(31) is False
    assert check_skip(x, [7, 18, 30]) == nodes
    assert x.remove(18) is True
    empty = SkipList(4)
    assert empty.remove(5) is False
    check_skip(empty, [])


def test_unlink_each_tower_level_and_clear_old_links():
    x = seed_skip([(7, 2), (18, 4), (30, 1), (42, 3)], 4)
    old = x.search(18)
    left = x.search(7)
    right = x.search(30)
    last = x.search(42)
    assert x.remove(18) is True
    assert x.head.forward[3] is None
    assert x.head.forward[2] is last
    assert x.head.forward[1] is left and left.forward[1] is last
    assert left.forward[0] is right and right.forward[0] is last
    assert old.forward == [None] * 4
    assert x.search(18) is None


def test_repair_tail_size_and_full_removal():
    x = SkipList(4)
    assert x.remove(5) is False
    for key, height in [(7, 2), (18, 4), (30, 1), (42, 3)]:
        x.insert(key, height)
    old = x.search(18)
    assert x.remove(18) is True
    assert old.forward == [None] * 4
    check_skip(x, [7, 30, 42])
    assert x.search(18) is None and x.remove(18) is False
    tail = x.search(42)
    assert x.remove(42) is True and tail.forward == [None] * 3
    check_skip(x, [7, 30])
    assert x.remove(7) is True
    check_skip(x, [30])
    assert x.remove(30) is True
    check_skip(x, [])
    assert x.insert(18, 1) is True and x.search(18) is not old
    check_skip(x, [18])
