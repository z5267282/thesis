def program():
    i = 0
    while i < 3:
        print(i)
        i += 1

from analyse import smart_trace
from line import Line
from tree_parser import parse

def test_while():
    root = parse(program)
    line_mapping = root.map_lines()
    execution = [
        Line(2),
        # loop iterations
        Line(3), Line(4), Line(5),
        Line(3), Line(4), Line(5),
        Line(3), Line(4), Line(5),
        # last loop iteration i = 3
        Line(3)
    ]
    filtered = smart_trace(line_mapping, execution)
    assert filtered == [
        Line(2),
        Line(3), Line(5)
    ]
