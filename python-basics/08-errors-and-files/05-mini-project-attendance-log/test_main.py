import ast
import inspect
import textwrap
from solution import total_charge, save_beacons, read_beacons

def test_total_charge():
    assert total_charge(["2", "bad", "4"]) == 6
    assert total_charge([]) == 0
    assert total_charge(["9", "no", "2", "0"]) == 11
    tree = ast.parse(textwrap.dedent(inspect.getsource(total_charge)))
    assert any(isinstance(n, ast.For) for n in ast.walk(tree)), "Use a loop to process entries."
    assert any(isinstance(n, ast.ExceptHandler) and isinstance(n.type, ast.Name) and n.type.id == "ValueError" for n in ast.walk(tree)), "Catch only ValueError for invalid counts."

def test_save_beacons():
    save_beacons(["5", "oops", "1"])
    with open("beacon-save.txt", "r", encoding="utf-8") as file:
        assert file.read() == "Charge: 6"
    original = save_beacons.__globals__["total_charge"]
    calls = []
    def tracked(entries):
        calls.append(entries)
        return 37
    try:
        save_beacons.__globals__["total_charge"] = tracked
        save_beacons(["fresh", "entries"])
        assert calls == [["fresh", "entries"]], "Call total_charge(entries) in save_beacons."
        with open("beacon-save.txt", "r", encoding="utf-8") as file:
            assert file.read() == "Charge: 37"
    finally:
        save_beacons.__globals__["total_charge"] = original

def test_read_beacons():
    with open("beacon-save.txt", "w", encoding="utf-8") as file:
        file.write("Shrine ready\nCharge: 7")
    assert read_beacons() == "Shrine ready\nCharge: 7"
