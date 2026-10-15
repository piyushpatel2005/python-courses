from solution import *


def test_function_binding():
    a, b = Greeter("Ari"), Greeter("Bo")
    first, second = bind_to(welcome, a), bind_to(welcome, b)
    assert first.__self__ is a and second.__self__ is b
    assert first.__func__ is welcome
    assert first("!") == "Welcome Ari!"
    a.name = "Cam"
    assert first(".") == "Welcome Cam." and second("?") == "Welcome Bo?"
    def length(self, extra):
        return len(self.name) + extra
    assert bind_to(length, b)(8) == 10
