import ast
import inspect
import textwrap
from solution import parse_command, charge_beacons, gate_open, play_mission


def test_parse_command():
    """Valid commands decode; invalid signals do not crash"""
    assert parse_command(" north:2 ") == ("NORTH", 2)
    assert parse_command("SOUTH:5") == ("SOUTH", 5)
    for bad in ("oops", ":3", "NORTH:no", "NORTH:0", "NORTH:-2"):
        assert parse_command(bad) is None, f"Ignore {bad!r}."
    tree = ast.parse(textwrap.dedent(inspect.getsource(parse_command)))
    assert any(isinstance(node, ast.Try) and any(isinstance(handler.type, ast.Name)
               and handler.type.id == "ValueError" for handler in node.handlers if handler.type)
               for node in ast.walk(tree)), "Catch ValueError for a bad signal number."


def test_charge_beacons():
    """Repeated valid commands charge only known beacons"""
    beacons = {"NORTH": 3, "SOUTH": 2, "EAST": 4}
    assert charge_beacons(beacons, ["north:2", "bad", "NORTH:1", "west:9", "south:2"]) == {
        "NORTH": 3, "SOUTH": 2, "EAST": 0}
    assert charge_beacons({"WEST": 8}, ["west:4", "west:-2", "west:1"]) == {"WEST": 5}
    namespace = charge_beacons.__globals__
    original = namespace["parse_command"]
    try:
        namespace["parse_command"] = lambda command: ("NORTH", 7) if command == "probe" else None
        assert charge_beacons({"NORTH": 9}, ["probe"]) == {"NORTH": 7}, (
            "Use parse_command inside charge_beacons.")
    finally:
        namespace["parse_command"] = original


def test_gate_open():
    """The gate needs every beacon, not merely one"""
    assert gate_open({"NORTH": 3, "SOUTH": 2}, {"NORTH": 3, "SOUTH": 2}) is True
    assert gate_open({"NORTH": 3, "SOUTH": 2}, {"NORTH": 9, "SOUTH": 1}) is False
    assert gate_open({"NORTH": 3}, {}) is False
    assert gate_open({}, {}) is False
    tree = ast.parse(textwrap.dedent(inspect.getsource(gate_open)))
    assert any(isinstance(n, ast.For) for n in ast.walk(tree)), "Check each beacon with a loop."
    assert any(isinstance(n, ast.If) for n in ast.walk(tree)), "Use a condition for the gate."


def test_play_mission():
    """A complete game has both a win and a graceful locked ending"""
    beacons = {"NORTH": 3, "SOUTH": 2}
    assert play_mission(beacons, ["north:2", "NORTH:1", "south:2"]) == [
        "NORTH: 3/3", "SOUTH: 2/2",
        "Exit Gate: OPEN - Ari leaves the Lantern Atlas with every beacon bright."]
    assert play_mission(beacons, ["north:3", "south:1"]) == [
        "NORTH: 3/3", "SOUTH: 1/2",
        "Exit Gate: LOCKED - Restore every beacon to continue."]
    assert play_mission({}, []) == ["Exit Gate: LOCKED - Restore every beacon to continue."]
    namespace = play_mission.__globals__
    original_charge, original_gate = namespace["charge_beacons"], namespace["gate_open"]
    try:
        namespace["charge_beacons"] = lambda beacons, commands: {"NORTH": 7}
        namespace["gate_open"] = lambda beacons, charges: charges["NORTH"] == 7
        assert play_mission({"NORTH": 9}, ["probe"]) == [
            "NORTH: 7/9", "Exit Gate: OPEN - Ari leaves the Lantern Atlas with every beacon bright."], (
            "Reuse charge_beacons and gate_open inside play_mission.")
    finally:
        namespace["charge_beacons"], namespace["gate_open"] = original_charge, original_gate
