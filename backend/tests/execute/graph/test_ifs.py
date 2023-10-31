from analyse import smart_trace
from execute import trace_program
from graph import generate_graphs
from line import Line
from tree_parser import parse

def program():
    i = 17
    if i % 2 == 0:
        print("found a two")
    elif i % 17 == 0:
        print("a fancy prime")
        print("fancy!")
    print("end of day!")

def test_ifs():
    root = parse(program)
    lines = trace_program(program)
    line_mapping = root.map_lines()
    filtered = smart_trace(line_mapping, lines)
    graphs = generate_graphs(filtered, line_mapping)

    assert filtered == [
        Line(8),
        Line(11),
        Line(13),
        Line(14)
    ]

    assert graphs == [
        [Line(8)],
        [Line(8), Line(11)],
        [Line(8), Line(11), Line(13)],
        [Line(8), Line(11), Line(13), Line(14)]
    ]
