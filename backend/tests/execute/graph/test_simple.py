def program():
    i = 1
    j = 1
    print(f"the sum is: {i + j}")

from analyse import smart_trace_all
from execute import trace_program
from graph import generate_graphs
from line import Line
from tree_parser import parse

def test_simple():
    root = parse(program)
    lines = trace_program(program)
    line_mapping = root.map_lines()
    filtered, = smart_trace_all(line_mapping, lines)
    graphs = generate_graphs(filtered, line_mapping)

    assert graphs == [
        [Line(4)],
        [Line(4), Line(4, event="return")]
    ]
