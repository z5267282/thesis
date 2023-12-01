def program():
    def msg():
        print("hi")
        print("bye")

    msg()

from analyse import smart_trace_all
from execute import trace_program
from line import Line
from tree_parser import parse

def test_simple():
    root = parse(program)
    line_mapping = root.map_lines()
    lines = trace_program(program)
    filtered = smart_trace_all(line_mapping, lines)

    assert filtered == [
        [Line(6, "line")],
        [Line(2, "call"), Line(4, "line"), Line(4, "return")],
        [Line(6, "return")]
    ]
