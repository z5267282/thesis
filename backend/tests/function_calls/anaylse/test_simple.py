def program():
    def msg():
        print("hi")
        print("bye")

    msg()

from analyse import smart_trace
from execute import trace_program
from line import Line
from tree_parser import parse

def test_simple():
    root = parse(program)
    line_mapping = root.map_lines()
    lines = trace_program(program)
    filtered = smart_trace(line_mapping, lines)

    assert filtered == [

    ]
