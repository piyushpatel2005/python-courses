from solution import *

def test_01_checkpoint():
    'In `merge_fronts`, merge current fronts until one run ends; return the prefix and both cursors.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    assert merge_fronts([1,4],[2,6])==([1,2,4],2,1)
    assert merge_fronts([2],[2])==([2],1,0)
    assert merge_fronts([],[3])==([],0,0)

def test_02_checkpoint():
    'In `merge_runs`, append both unconsumed suffixes and return the completed merge.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    for left, right in [([], []), ([1], []), ([], [2]), ([1, 3, 3], [2, 3, 8]), ([-4, 0], [-3, 5])]:
        a, b = left[:], right[:]
        result = merge_runs(left, right)
        assert result == sorted(a + b)
        assert result is not left and result is not right
        assert left == a and right == b
    class Item:
        def __init__(self, key, tag): self.key, self.tag = key, tag
        def __lt__(self, other): return self.key < other.key
    left = [Item(1, 'a'), Item(3, 'b')]
    right = [Item(1, 'c'), Item(3, 'd')]
    assert [x.tag for x in merge_runs(left, right)] == ['a', 'c', 'b', 'd']

