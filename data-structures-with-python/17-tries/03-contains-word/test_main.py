from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_follow_word():
    'Follow the character path and return `False` at the first missing edge.'
    trie = Trie()
    trie.insert('oak')
    def snapshot(node):
        return (node.terminal, {char: snapshot(child) for char, child in node.children.items()})
    before = snapshot(trie.root)
    for query in ['x', 'oz', 'oaks']:
        assert trie.contains(query) is False
    assert snapshot(trie.root) == before


def test_finish_contains():
    'After a complete walk, return the final terminal marker.'
    trie = Trie()
    assert trie.contains('') is False
    for word in ['oak', 'oaks', 'Oak']:
        trie.insert(word)
    assert trie.contains('oak') is True
    assert trie.contains('oa') is False
    assert trie.contains('Oak') is True
    trie.insert('')
    assert trie.contains('') is True
