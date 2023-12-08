def program():
    def a():
        print("a")

    i = 0
    if i == 1:
        print("one")
    else:
        print("hi")
        a()

from analyse import smart_trace_all
from execute import trace_program
from line import Line
from tree_parser import parse

def test_conditional():
    lines = trace_program(program)
    assert lines == [
        [Line(1, "call"), Line(5, "line"), Line(6, "line"), Line(9, "line"), Line(10, "line")],
        [Line(2, "call"), Line(3, "line"), Line(3, "return")],
        [Line(10, "return")]
    ]

    call = lines[0][3]
    assert call.line_no == 9
    assert call.output == ["hi\n"]

    root = parse(program)
    line_mapping = root.map_lines()
    filtered = smart_trace_all(line_mapping, lines)
    assert filtered == [
        [Line(5, "line"), Line(8, "line"), Line(10, "line")],
        [Line(2, "call"), Line(3, "line"), Line(3, "return")],
        [Line(10, "return")]
    ]
