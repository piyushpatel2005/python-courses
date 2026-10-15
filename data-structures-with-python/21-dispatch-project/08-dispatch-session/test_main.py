from solution import *


def test_one_command_recovery():
    class Desk:
        def execute(self, command):
            if command[0] == "key":
                raise KeyError("x")
            if command[0] == "value":
                raise ValueError("x")
            if command[0] == "bug":
                raise RuntimeError("bug")
            return command[0]

    d = Desk()
    assert execute_safely(d, ("ok",)) == "ok"
    assert (
        execute_safely(d, ("key",)) == "error"
        and execute_safely(d, ("value",)) == "error"
    )
    try:
        execute_safely(d, ("bug",))
    except RuntimeError:
        pass
    else:
        assert False


def test_collect_session_results_in_order():
    import solution as submitted

    calls = []
    original = submitted.execute_safely

    def safe(workbench, command):
        calls.append(command)
        return command[0]

    submitted.execute_safely = safe
    try:
        desk = object()
        assert run_session(desk, [("first",), ("error",), ("last",)]) == [
            "first",
            "error",
            "last",
        ]
        assert calls == [("first",), ("error",), ("last",)]
        assert run_session(desk, []) == []
    finally:
        submitted.execute_safely = original
