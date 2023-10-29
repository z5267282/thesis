def program():
    i = 1
    twos, sevens = 0, 0
    while i < 8:
        if i % 2 == 0:
            print("two")
            twos += 1
        elif i % 7 == 0:
            print("seven")
            sevens += 1
        i += 1

    print(f"2s: {twos}, 7s: {sevens}")

from analyse import smart_trace
from graph import generate_graphs
from line import Line
from tree_parser import parse

def test_while_1d():
    root = parse(program)
    line_mapping = root.map_lines()
    execution = [
        # top-level
        Line(2, {}), Line(3, {}),
        # loop
        Line(4, {}), Line(5, {}), Line(8, {}), Line(11, {}),
        Line(4, {}), Line(5, {}), Line(6, {}), Line(7, {}), Line(11, {}),
        Line(4, {}), Line(5, {}), Line(8, {}), Line(11, {}),
        Line(4, {}), Line(5, {}), Line(6, {}), Line(7, {}), Line(11, {}),
        Line(4, {}), Line(5, {}), Line(8, {}), Line(11, {}),
        Line(4, {}), Line(5, {}), Line(6, {}), Line(7, {}), Line(11, {}),
        Line(4, {}), Line(5, {}), Line(8, {}), Line(9, {}), Line(10, {}),
            Line(11, {}),
        # breaking the loop
        Line(4, {}),
        # end
        Line(13, {})
    ]
    filtered = smart_trace(execution)
    graphs = generate_graphs(filtered, line_mapping)
