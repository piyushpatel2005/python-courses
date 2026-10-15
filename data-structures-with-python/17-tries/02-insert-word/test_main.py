from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_insert_path():
    'Walk the characters, reusing existing children and allocating only missing nodes.'
    trie, other = Trie(), Trie()
    trie.insert('pine')
    branch = trie.root.children['p']
    trie.insert('pit')
    trie.insert('pine')
    assert trie.root.children['p'] is branch
    assert set(branch.children['i'].children) == {'n', 't'}
    assert 'e' in branch.children['i'].children['n'].children
    assert other.root.children == {}


def test_mark_word_end():
    'Mark only the node reached after the last character as terminal.'
    trie = Trie()
    trie.insert('pin')
    assert trie.root.terminal is False
    assert trie.root.children['p'].terminal is False
    assert trie.root.children['p'].children['i'].children['n'].terminal is True
    trie.insert('')
    assert trie.root.terminal is True
