from solution import *


def test_deferred_method_remembers_its_tool():
    first, second = Tool(2), Tool(9)
    action, other = deferred_use(first), deferred_use(second)
    assert callable(action), "Return tool.record_use without parentheses."
    assert getattr(action, "__self__", None) is first, "Return the bound method itself."
    assert first.uses == 2 and second.uses == 9, "Do not call the method while selecting it."
    first.uses = 6
    assert action() == 7 and first.uses == 7 and second.uses == 9
    assert action() == 8 and other() == 10
