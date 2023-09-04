from analyse import smart_trace
from execute import trace_program
from graph import generate_graphs
from line import Line
from tree_parser import parse


def program():
    i = 1
    j = 1
    print(f"the sum is: {i + j}")


def test_simple():
    root = parse(program)
    lines = trace_program(program)
    line_mapping = root.map_lines()
    filtered = smart_trace(line_mapping, lines)
    graphs = generate_graphs(filtered, line_mapping)

    assert graphs == [
        [Line(10, {})]
    ]
