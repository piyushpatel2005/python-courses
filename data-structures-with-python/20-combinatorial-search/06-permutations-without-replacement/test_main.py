from solution import *


def test_available_permutation_positions():
    assert unused_indices([True, False, False, True]) == [1, 2]
    assert unused_indices([]) == [] and unused_indices([True]) == []


def test_choose_one_permutation_position():
    path = [8]
    used = [True, False, False]
    choose_position([8, 2, 6], 2, path, used)
    assert path == [8, 6] and used == [True, False, True]


def test_restore_permutation_state():
    path = [8, 6]
    used = [True, False, True]
    release_position(2, path, used)
    assert path == [8] and used == [True, False, False]
    release_position(0, path, used)
    assert path == [] and used == [False, False, False]
