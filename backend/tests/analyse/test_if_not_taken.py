def program():
    i = 3
    if i % 2 == 0:
        print("an even")
        print("yeah")
    print("the end pal")

from analyse import smart_trace
from line import Line
from tree_parser import parse

def test_if_not_taken():
    root = parse(program)
    line_mapping = root.map_lines()
    execution = [Line(2, {}), Line(3, {}), Line(6, {})]
    assert smart_trace(line_mapping, execution) == [
        Line(2, {}), Line(6, {})
    ]
