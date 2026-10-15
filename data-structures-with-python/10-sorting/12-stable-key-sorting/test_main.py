from solution import *

def test_01_checkpoint():
    'In `shift_records`, shift records with larger keys and return the gap position.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    a=[(1,'x'),(4,'z'),(4,'a'),(2,'q')]
    assert shift_records(a,3,2,lambda row:row[0])==1
    assert a==[(1,'x'),(4,'z'),(4,'z'),(4,'a')]
    assert shift_records([(2,'z'),(2,'a')],1,2,lambda row:row[0])==1

def test_02_checkpoint():
    'In `insert_record`, fill the returned gap with the saved original record.'
    import ast
    import solution
    from pathlib import Path
    tree = ast.parse(Path(solution.__file__).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = getattr(node.func, "id", getattr(node.func, "attr", ""))
            assert name not in {"sorted", "sort", "heapify", "heappush", "heappop", "nsmallest", "nlargest"}, "Use the taught algorithm rather than a library shortcut."
    a = [{'rank': 2, 'id': 'z'}, {'rank': 1, 'id': 'q'}, {'rank': 2, 'id': 'a'}]
    before = a[:]
    result = stable_key_sort(a, lambda row: row['rank'])
    assert [x['id'] for x in result] == ['q', 'z', 'a']
    assert a == before and result is not a
    assert result[0] is a[1] and result[1] is a[0]
    assert stable_key_sort([], lambda x: x) == []
    assert stable_key_sort([3, -2, 3, 1], lambda x: -x) == [3, 3, 1, -2]

