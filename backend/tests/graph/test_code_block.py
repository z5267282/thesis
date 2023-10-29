def program():
    i = 42
    j = 69
    print(f"{i} + {j} = {i + j}")

from analyse import smart_trace
from generate import generate_graphs
from line import Line
from tree_parser import parse

def test_code_block():
    root = parse(program)
    line_mapping = root.map_lines()
    execution = [Line(2, {}), Line(3, {}), Line(4, {})]
    filtered = smart_trace(line_mapping, execution)
    graphs = generate_graphs(filtered, line_mapping)
    assert graphs == [
        [Line(4, {})]
    ]
