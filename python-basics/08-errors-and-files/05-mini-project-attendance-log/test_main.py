import ast
import inspect
import textwrap
from solution import total_arrivals, save_log, read_log

def test_total_arrivals():
    assert total_arrivals(["2", "bad", "4"]) == 6
    assert total_arrivals([]) == 0
    assert total_arrivals(["9", "no", "2", "0"]) == 11
    tree = ast.parse(textwrap.dedent(inspect.getsource(total_arrivals)))
    assert any(isinstance(n, ast.For) for n in ast.walk(tree)), "Use a loop to process entries."
    assert any(isinstance(n, ast.ExceptHandler) and isinstance(n.type, ast.Name) and n.type.id == "ValueError" for n in ast.walk(tree)), "Catch only ValueError for invalid counts."

def test_save_log():
    save_log(["5", "oops", "1"])
    with open("attendance-log.txt", "r", encoding="utf-8") as file:
        assert file.read() == "Arrivals: 6"

def test_read_log():
    with open("attendance-log.txt", "w", encoding="utf-8") as file:
        file.write("Shift complete\nArrivals: 7")
    assert read_log() == "Shift complete\nArrivals: 7"
