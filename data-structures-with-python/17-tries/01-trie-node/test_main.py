from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_fresh_children():
    'Give each node its own empty `children` dictionary.'
    first, second = TrieNode(), TrieNode()
    assert first.children == {} and second.children == {}
    first.children['x'] = TrieNode()
    assert second.children == {}


def test_terminal_flag():
    "Set each new node's `terminal` marker to `False`."
    first, second = TrieNode(), TrieNode()
    assert first.terminal is False and second.terminal is False
    first.terminal = True
    assert second.terminal is False
