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

def test_skip_predecessor_identity():
    x=seed_skip([(5,1),(12,3),(19,2),(31,1)],4)
    nodes=check_skip(x,[5,12,19,31]); h=x.head
    assert x.predecessors(12)==[nodes[0],h,h,h]
    assert x.predecessors(20)==[nodes[2],nodes[2],nodes[1],h]
    assert x.predecessors(-1)==[h]*4
    assert x.predecessors(99)==[nodes[3],nodes[2],nodes[1],h]
    empty=SkipList(2); assert empty.predecessors(8)==[empty.head]*2
    check_skip(x,[5,12,19,31])
    class CountedInt(int):
        comparisons=0
        def __lt__(self,other):
            CountedInt.comparisons+=1
            return int(self)<int(other)
    pairs=[]
    for key in range(1,65):
        height=1
        while height<7 and key % (2 ** height)==0:
            height+=1
        pairs.append((CountedInt(key),height))
    tower=seed_skip(pairs,7)
    CountedInt.comparisons=0
    result=tower.predecessors(64)
    assert result[0].key==63
    assert CountedInt.comparisons<=20, "Use upper levels instead of scanning the base chain"
