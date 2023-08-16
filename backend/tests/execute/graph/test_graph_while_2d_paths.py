from analyse import smart_trace
from execute import trace_program
from graph import generate_graphs
from line import Line
from tree_parser import parse

def program():
    i = 1
    twos, fives = 0, 0
    while i < 6:
        if i % 2 == 0:
            print("two")
            twos += 1
        elif i % 5 == 0:
            print("five")
            fives += 1

        j = 0
        while j < i:
            print("X", end="")
            j += 1

        i += 1

    print(f"2s: {twos}, 5s: {fives}")

def test_graph_simple():
    root = parse(program)
    lines = trace_program(program)
    line_mapping = root.map_lines()
    filtered = smart_trace(line_mapping, lines)
    graphs = generate_graphs(filtered, line_mapping)

    assert filtered == [
        # outer
        Line(9, {}),
        # i = 1
        Line(10, {}),
        Line(18, {}),
        Line(19, {}),
        Line(21, {}),
        Line(23, {}),
        # i = 2
        Line(10, {}),
        Line(11, {}),
        Line(13, {}),
        Line(18, {}),
        Line(19, {}),
        Line(21, {}),
        Line(23, {}),
        # i = 5
        Line(10, {}),
        Line(14, {}),
        Line(16, {}),
        Line(18, {}),
        Line(19, {}),
        Line(21, {}),
        Line(23, {}),
        # end
        Line(25, {})
    ]
