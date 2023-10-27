def program():
    i = 3
    if i % 2 == 0:
        print("an even")
        print("yeah")
    else:
        print("an odd number")
        print("wicked!")
    print("the end pal")

from analyse import smart_trace
from line import Line
from tree_parser import parse

def test_if_not_taken():
    root = parse(program)
    line_mapping = root.map_lines()
    execution = [
        Line(2, {}),
        # if statement
        # note the else itself does not get directly executed
        Line(3, {}), Line(7, {}), Line(8, {}),
        Line(9, {})
    ]
    assert smart_trace(line_mapping, execution) == [
        Line(2, {}),
        # the else should artifically appear in the smart trace
        Line(6, {}), Line(8, {}),
        Line(9, {})
    ]
