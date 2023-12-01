def program():
    def msg():
        print("hi")
        print("bye")

    a = 0
    if a % 2 == 1:
        print("odd")
    else:
        print("even")
        msg()

from analyse import smart_trace_all
from execute import trace_program
from line import Line
from tree_parser import parse

def test_conditional():
    root = parse(program)
    line_mapping = root.map_lines()
    lines = trace_program(program)
    filtered = smart_trace_all(line_mapping, lines)
    assert filtered == [
        [Line(6, "line"), Line(9, "line"), Line(11, "line")],
        [Line(2, "call"), Line(4, "line"), Line(4, "return")],
        [Line(11, "return")]
    ]
