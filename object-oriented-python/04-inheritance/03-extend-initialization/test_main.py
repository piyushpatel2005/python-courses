from solution import *


def test_01_extend_initialization():
    for title, hour in (("Exhibit", 14), ("Tour", 9), ("", 0)):
        ticket = TimedTicket(title, hour)
        assert ticket.title == title and ticket.hour == hour
        assert ticket.label() == f"Ticket: {title}"
    calls = []
    original = Ticket.__init__
    try:
        def tracking(self, title):
            calls.append(title)
            self.title = title.upper()
        Ticket.__init__ = tracking
        item = TimedTicket("evening", 18)
        assert calls == ["evening"], "Delegate base initialization once."
        assert item.title == "EVENING" and item.hour == 18
    finally:
        Ticket.__init__ = original
    import ast, inspect, textwrap
    source = ast.parse(textwrap.dedent(inspect.getsource(TimedTicket.__init__)))
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "super" for node in ast.walk(source)), "Use super() for the base initializer."
