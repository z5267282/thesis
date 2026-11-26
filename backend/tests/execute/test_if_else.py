def program():
    i = 0
    if i == 1:
        print("one")
    else:
        print("something else")

from analyse import smart_trace_all
from execute import trace_program
from line import Line
from tree_parser import parse

def test_if_else():
    all_lines = trace_program(program)
    assert all_lines == [
        [
            Line(1, event="call"),
            Line(2), Line(3), Line(6),
            Line(6, event="return")
        ]
    ]
    root = parse(program)
    filtered, = smart_trace_all(root.map_lines(), all_lines)
    assert filtered == [
        Line(2), Line(5), Line(6),
        Line(6, event="return")
    ]
