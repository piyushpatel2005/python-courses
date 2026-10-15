from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_bundle_keys():
    'Convert each request to a frozenset key, ignoring its order and inner duplicates.'
    result = count_bundles([['lamp', 'stand'], ['stand', 'lamp', 'lamp'], []])
    assert set(result) == {frozenset(['lamp', 'stand']), frozenset()}
    assert all(type(key) is frozenset for key in result)


def test_bundle_counts():
    'Accumulate the number of requests for each key instead of overwriting its count.'
    assert count_bundles([[9], [9], [8]]) == {frozenset([9]): 2, frozenset([8]): 1}
    assert count_bundles([[], []]) == {frozenset(): 2}
    assert count_bundles([]) == {}
    source = [['a'], ['a']]
    result = count_bundles(source)
    source[0].append('b')
    assert result == {frozenset(['a']): 2}
