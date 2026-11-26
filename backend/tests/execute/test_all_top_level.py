def program():
    i = 42
    j = 69
    print(f"{i} + {j} = {i + j}")

from execute import trace_program
from line import Line

def test_all_top_level():
    filtered, = trace_program(program)
    assert filtered == [
        Line(1, event="call"),
        Line(2), Line(3), Line(4),
        Line(4, event="return")
    ]
