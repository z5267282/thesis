def program():
    i = 0
    if i % 2 == 0:
        print("an even")
        print("yeah")

from analyse import smart_trace
from line import Line
from tree_parser import parse

def test_if_simple():
    root = parse(program)
    line_mapping = root.map_lines()
    execution = [
        Line(2),
        # if statement-related
        Line(3), Line(4), Line(5)
    ]
    assert smart_trace(line_mapping, execution) == [
        Line(2), Line(3), Line(5)
    ]
