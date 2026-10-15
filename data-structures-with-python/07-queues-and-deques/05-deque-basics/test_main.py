from solution import *



def test_01_step():
    "Implement the `right` command with a rear append."
    assert process_deque([("right", 3), ("right", 7)]) == ([], [3, 7])


def test_02_step():
    "Implement the `left` command with a front append."
    assert process_deque([("left", 3), ("left", 7)]) == ([], [7, 3])


def test_03_step():
    "Implement `take_left`, recording the removed value only when an item exists."
    assert process_deque([("take_left", None), ("right", 3), ("right", 7), ("take_left", None)]) == ([3], [7])


def test_04_step():
    "Implement `take_right` with the same empty-removal policy."
    assert process_deque([("take_right", None), ("right", 3), ("right", 7), ("take_right", None)]) == ([7], [3])


def test_05_complete_behavior():
    "Raise `ValueError` for an unknown command."
    commands = [("take_left", None), ("right", 2), ("left", 1), ("right", 3), ("take_right", None), ("take_left", None)]
    saved = commands[:]
    assert process_deque(commands) == ([3, 1], [2])
    assert commands == saved and process_deque([]) == ([], [])
    assert process_deque([("left", None), ("take_right", 0)]) == ([None], [])
    try:
        process_deque([("unknown", 1)])
    except ValueError:
        pass
    else:
        assert False, "Reject unknown commands"
    import ast, solution
    with open(solution.__file__) as f: tree = ast.parse(f.read())
    assert any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "deque" for n in ast.walk(tree)), "Use collections.deque"
