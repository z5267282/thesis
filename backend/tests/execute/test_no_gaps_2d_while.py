def program():
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            print("X", end="")
            j += 1
        i += 1
        print("")
    print("done")

from analyse import smart_trace_all
from execute import trace_program
from line import Line
from tree_parser import parse

def test_no_gaps_2d_while():
    root = parse(program)
    line_mapping = root.map_lines()
    lines = trace_program(program)
    filtered, = smart_trace_all(line_mapping, lines)

    assert filtered == [
        # top level
        Line(2),
        # outer loop pre
        Line(3), Line(4),
        # inner loop
        Line(5), Line(7),
        # outer loop post
        Line(9),
        # top level
        Line(10), Line(10, event="return")
    ]
