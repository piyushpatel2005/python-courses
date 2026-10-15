from solution import *

def test_balanced_nested_types():
    for text in ["", "words only", "[]", "{x[2+(3)]}", "()[]{}", "((()))"]:
        assert balanced(text) is True, text
    for text in ["(", ")", "([)]", "{]", "(()", "[]}", "][]["]:
        assert balanced(text) is False, text
    assert balanced("([{}])") is True
    original=Stack.push; seen=[]
    def observed(self,value):
        seen.append(value); return original(self,value)
    Stack.push=observed
    try:
        assert balanced("([x])") is True and seen==['(', '[']
    finally:
        Stack.push=original
