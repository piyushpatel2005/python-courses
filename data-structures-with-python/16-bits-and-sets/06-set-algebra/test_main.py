from solution import *

def expect_error(kind, operation):
    try:
        operation()
    except kind:
        return
    raise AssertionError("Expected " + kind.__name__)


def test_group_either():
    'Fill `either` with the union of the two local sets.'
    for left, right in [([], []), ([2, 2, 3], [3, 5]), ([7], []), ([], [8])]:
        a, b = set(left), set(right)
        result = compare_groups(left, right)['either']
        assert type(result) is set and result == a | b
    left, right = {2, 4}, {4, 9}
    answer = compare_groups(left, right)['either']
    answer.add(100)
    assert left == {2, 4} and right == {4, 9}


def test_group_both():
    'Fill `both` with their intersection.'
    for left, right in [([], []), ([2, 2, 3], [3, 5]), ([7], []), ([], [8])]:
        a, b = set(left), set(right)
        result = compare_groups(left, right)['both']
        assert type(result) is set and result == a & b
    left, right = {2, 4}, {4, 9}
    answer = compare_groups(left, right)['both']
    answer.add(100)
    assert left == {2, 4} and right == {4, 9}


def test_group_left_only():
    'Fill `left_only` with members of the left set absent from the right.'
    for left, right in [([], []), ([2, 2, 3], [3, 5]), ([7], []), ([], [8])]:
        a, b = set(left), set(right)
        result = compare_groups(left, right)['left_only']
        assert type(result) is set and result == a - b
    left, right = {2, 4}, {4, 9}
    answer = compare_groups(left, right)['left_only']
    answer.add(100)
    assert left == {2, 4} and right == {4, 9}


def test_group_exclusive():
    'Fill `exclusive` with members present in exactly one set.'
    for left, right in [([], []), ([2, 2, 3], [3, 5]), ([7], []), ([], [8])]:
        a, b = set(left), set(right)
        result = compare_groups(left, right)['exclusive']
        assert type(result) is set and result == a ^ b
    left, right = {2, 4}, {4, 9}
    answer = compare_groups(left, right)['exclusive']
    answer.add(100)
    assert left == {2, 4} and right == {4, 9}
