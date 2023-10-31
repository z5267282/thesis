def program():
    i = 3
    while i < 3:
        print(i)
        i += 1
    print("that's all kids")

from analyse import smart_trace
from line import Line
from tree_parser import parse

def test_while_not_taken():
    root = parse(program)
    line_mapping = root.map_lines()
    execution = [Line(2), Line(3), Line(6)]
    filtered = smart_trace(line_mapping, execution)
    assert filtered == [Line(2), Line(6)]
