from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_locate_collection_prefix():
    'Follow the prefix and return an empty list if its path is missing.'
    trie = Trie()
    trie.insert('ant')
    assert trie.collect('x') == []
    assert trie.collect('az') == []
    assert trie.collect('ants') == []


def test_append_current_word():
    'In `visit`, append the current spelling if this node is terminal.'
    trie = Trie()
    trie.insert('an')
    assert trie.collect('an') == ['an']
    empty = Trie()
    empty.insert('')
    assert empty.collect('') == ['']


def test_collect_terminal_words():
    'In `visit`, recurse through child edges in sorted character order.'
    trie = Trie()
    words = ['', 'an', 'ant', 'angle', 'bat', 'ant', 'An']
    for word in words:
        trie.insert(word)
    for prefix in ['', 'an', 'ant', 'b']:
        assert trie.collect(prefix) == sorted({w for w in words if w.startswith(prefix)})
    result = trie.collect('an')
    result.clear()
    assert trie.collect('an') == ['an', 'angle', 'ant']
    assert Trie().collect('') == []
