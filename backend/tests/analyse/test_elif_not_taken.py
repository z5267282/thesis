def program():
    i = 3
    if i % 2 == 0:
        print("an even")
        print("yeah")
    elif i % 17 == 0:
        print("a fancy prime number")
    elif i % 23 == 0:
        print("23!")
    print("the end pal")

from analyse import smart_trace
from line import Line
from tree_parser import parse

def test_elif_not_taken():
    root = parse(program)
    execution = [
        Line(2, {}),
        # branches
        Line(3, {}), Line(6, {}), Line(8, {}),
        Line(10, {})
    ]
    assert smart_trace(root.map_lines(), execution) == [
        Line(2, {}), Line(10, {})
    ]
