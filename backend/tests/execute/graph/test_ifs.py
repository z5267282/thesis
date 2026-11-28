def program():
    i = 17
    if i % 2 == 0:
        print("found a two")
    elif i % 17 == 0:
        print("a fancy prime")
        print("fancy!")
    print("end of day!")

from analyse import smart_trace_all
from execute import trace_program
from graph import generate_graphs
from line import Line
from tree_parser import parse

def test_ifs():
    root = parse(program)
    lines = trace_program(program)
    line_mapping = root.map_lines()
    filtered, = smart_trace_all(line_mapping, lines)
    graphs = generate_graphs(filtered, line_mapping)

    assert filtered == [
        Line(2),
        Line(5), Line(7),
        Line(8), Line(8, event="return")
    ]

    assert graphs == [
        [Line(2)],
        [Line(2), Line(5)],
        [Line(2), Line(5), Line(7)],
        [Line(2), Line(5), Line(7), Line(8)],
        [Line(2), Line(5), Line(7), Line(8), Line(8, event="return")]
    ]
