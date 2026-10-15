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

def test_postfix_parses_integer_tokens():
    original=Stack.push; seen=[]
    def observed(self,value):
        seen.append(value)
        return original(self,value)
    Stack.push=observed
    try:
        for token, expected in [('-6',-6),('0',0),('12',12)]:
            postfix([token])
            assert seen[-1]==expected
        assert len(seen)==3
        expect_error(ValueError,lambda:postfix(['oops']))
    finally:
        Stack.push=original


def test_postfix_combines_two_operands_in_order():
    # Supply operands locally so this check tests the operator branch alone.
    original=postfix.__globals__['Stack']; created=[]
    def seeded():
        stack=original()
        stack.push(8); stack.push(3)
        stack.pushed=[]
        push=stack.push
        def observed(value):
            stack.pushed.append(value)
            return push(value)
        stack.push=observed
        created.append(stack)
        return stack
    postfix.__globals__['Stack']=seeded
    try:
        postfix(['-'])
        assert created[-1].pushed==[5]
    finally:
        postfix.__globals__['Stack']=original
    def empty():
        return original()
    postfix.__globals__['Stack']=empty
    try:
        expect_error(ValueError,lambda:postfix(['+']))
    finally:
        postfix.__globals__['Stack']=original


def test_postfix_order_and_errors():
    assert postfix(["12","5","-"])==7
    assert postfix(["3","4","+","2","*"])==14
    assert postfix(["-6","2","*"])==-12
    assert postfix(["0"])==0
    assert postfix(["20","3","2","*","-"])==14
    for tokens in [[],["2","3"],["+"],["1","-"],["oops"],["2","3","/"],["2","3","+","*"]]:
        expect_error(ValueError,lambda tokens=tokens:postfix(tokens))
    assert postfix(["5"])==5
    original=Stack.pop; calls=[]
    def observed(self):
        calls.append(True); return original(self)
    Stack.pop=observed
    try:
        assert postfix(["8","3","-"])==5 and len(calls)==3
    finally:
        Stack.pop=original
