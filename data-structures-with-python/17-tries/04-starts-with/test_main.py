from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_follow_prefix():
    'Follow the character path and return `False` at the first missing edge.'
    trie = Trie()
    trie.insert('oak')
    def snapshot(node):
        return (node.terminal, {char: snapshot(child) for char, child in node.children.items()})
    before = snapshot(trie.root)
    for query in ['x', 'oz', 'oaks']:
        assert trie.starts_with(query) is False
    assert snapshot(trie.root) == before


def test_finish_starts_with():
    'After a complete walk, return `True`, including for the empty prefix.'
    trie = Trie()
    assert trie.starts_with('') is True
    trie.insert('stone')
    for prefix in ['', 's', 'st', 'stone']:
        assert trie.starts_with(prefix) is True
    assert trie.contains('st') is False
