def program():
    i = 0
    if i == 1:
        print("one")
    else:
        print("something else")

from execute import trace_program
from line import Line

def test_if_else():
    lines = trace_program(program)
    assert lines == [ Line(2, {}), Line(5, {}), Line(6, {}) ]
