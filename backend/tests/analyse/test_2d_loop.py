def program():
    i = 0
    while i < 2:
        j = 0
        while j <= i:
            print(j, end=", ")
            j += 1
        i += 1

from analyse import smart_trace
from line import Line
from tree_parser import parse

def test_2d_loop():
    root = parse(program)
    execution = [
        Line(2),
        # i = 0
        Line(3), Line(4),
            # j = 0
            Line(5), Line(6), Line(7),
            # j = 1
            Line(5),
        Line(8),
        # i =  1
        Line(3), Line(4),
            # j = 0
            Line(5), Line(6), Line(7),
            # j = 1
            Line(5), Line(6), Line(7),
            # j = 2
            Line(5),
        Line(8),
        # ending the loop
        Line(3)
    ]
    assert smart_trace(root.map_lines(), execution) == [
        Line(2),
        # loop iteration
        Line(3), Line(4),
            Line(5), Line(7),
        Line(8)
    ]
