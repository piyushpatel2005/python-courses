from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_find_deletion_target():
    'Follow the word while saving its edges; return `False` for a missing path or nonterminal endpoint.'
    trie = Trie()
    trie.insert('cart')
    for word in ['x', 'cars', 'car', '']:
        assert trie.delete(word) is False
    assert trie.collect('') == ['cart']


def test_unmark_deleted_word():
    "Clear the matched node's terminal flag without changing its children."
    trie = Trie()
    for word in ['car', 'cart', 'cat', 'car', '']:
        trie.insert(word)
    assert trie.delete('car') is True
    assert trie.contains('car') is False
    assert trie.contains('cart') is True and trie.contains('cat') is True
    assert trie.delete('car') is False
    assert trie.delete('') is True and trie.contains('') is False


def test_prune_unused_suffix():
    'Walk the saved edges backward and detach only childless, nonterminal nodes; stop at the first needed node.'
    trie = Trie()
    for word in ['car', 'cart', 'cat']:
        trie.insert(word)
    trie.delete('cart')
    assert trie.contains('car') and trie.contains('cat')
    assert 't' not in trie.root.children['c'].children['a'].children['r'].children
    trie.delete('car')
    assert set(trie.root.children['c'].children['a'].children) == {'t'}
    trie.delete('cat')
    assert trie.root.children == {}
    trie.insert('new')
    assert trie.contains('new')
