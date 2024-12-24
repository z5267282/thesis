def program():
    def a():
        print("a")

    print("start")
    a()
    print("end")

from analyse import smart_trace_all
from execute import trace_program
from line import Line
from tree_parser import parse

def test_embedded_code_block_call():
    root = parse(program)
    line_mapping = root.map_lines()
    lines = trace_program(program)
    filtered = smart_trace_all(line_mapping, lines)

    assert filtered == [
        [Line(6, "line")],
        [Line(2, "call"), Line(3, "line"), Line(3, "return")],
        [Line(7, "line"), Line(7, "return")]
    ]
