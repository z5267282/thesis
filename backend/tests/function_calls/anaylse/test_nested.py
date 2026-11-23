def program():
    def a():
        print("a")
        b()

    def b():
        print("b")

    print("start")
    a()
    print("end")

from analyse import smart_trace_all
from execute import trace_program
from line import Line
from tree_parser import parse

def test_nested():
    root = parse(program)
    line_mapping = root.map_lines()
    lines = trace_program(program)
    filtered = smart_trace_all(line_mapping, lines)

    assert filtered == [
        [Line(10, "line")],
        [Line(2, "call"), Line(4, "line")],
        [Line(6, "call"), Line(7, "line"), Line(7, "return")],
        [Line(4, "return")],
        [Line(11, "line"), Line(11, "return")]
    ]
