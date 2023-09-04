from analyse import smart_trace
from execute import trace_program
from graph import generate_graphs
from line import Line
from tree_parser import parse


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


def test_while_1d():
    root = parse(program)
    lines = trace_program(program)
    line_mapping = root.map_lines()
    filtered = smart_trace(line_mapping, lines)
    graphs = generate_graphs(filtered, line_mapping)

    assert filtered == [
        Line(9, {}),
        Line(10, {}),
        Line(17, {}),
        Line(10, {}),
        Line(11, {}),
        Line(13, {}),
        Line(17, {}),
        Line(10, {}),
        Line(14, {}),
        Line(16, {}),
        Line(17, {}),
        Line(19, {})
    ]

    assert graphs == [
        [Line(9, {})],
        [Line(9, {}), Line(10, {})],
        [Line(9, {}), Line(10, {}), Line(17, {})],
        [Line(9, {}), Line(10, {})],
        [Line(9, {}), Line(10, {}), Line(11, {})],
        [Line(9, {}), Line(10, {}), Line(11, {}), Line(13, {})],
        [Line(9, {}), Line(10, {}), Line(11, {}), Line(13, {}), Line(17, {})],
        [Line(9, {}), Line(10, {})],
        [Line(9, {}), Line(10, {}), Line(14, {})],
        [Line(9, {}), Line(10, {}), Line(14, {}), Line(16, {})],
        [Line(9, {}), Line(10, {}), Line(14, {}), Line(16, {}), Line(17, {})],
        [Line(9, {}), Line(19, {})]
    ]
