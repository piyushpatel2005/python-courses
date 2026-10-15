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

def test_minimum_stack_prefix_summaries():
    x=MinStack(); other=MinStack(); expect_error(IndexError,x.minimum)
    expect_error(IndexError,x.pop)
    model=[]
    for value in [8,3,3,6,-2,-2,9]:
        assert x.push(value) is None; model.append(value)
        assert len(x)==len(model) and x.minimum()==min(model)
        assert x.entries.peek()==(value,min(model))
    while model:
        assert x.pop()==model.pop()
        if model: assert x.minimum()==min(model)
    expect_error(IndexError,x.minimum); expect_error(IndexError,x.pop)
    assert len(other)==0
    x.push(0); assert x.minimum()==0 and x.pop()==0
    for value in range(60,0,-1):
        x.push(value)
    class ReadBudget(list):
        reads=0
        def __iter__(self):
            raise AssertionError("Use the previous minimum; do not scan entries")
        def __getitem__(self,index):
            self.reads+=1
            assert self.reads<=3, "A push must read only the previous summary"
            return super().__getitem__(index)
    x.entries.items=ReadBudget(x.entries.items)
    x.push(5)
    assert x.minimum()==1 and len(x)==61
