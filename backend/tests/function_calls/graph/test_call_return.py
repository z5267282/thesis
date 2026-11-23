def program():
    def a():
        print("a")
    
    a()

from graph import generate_graphs
from line import Line
from tree_parser import parse

def test_call_return():
    """Graphs for a function call region should preserve the call and return lines."""
    root = parse(program)
    line_mapping = root.map_lines()
    graphs = generate_graphs(
        [Line(2, "call"), Line(3, "line"), Line(3, "return")], line_mapping
    )

    assert graphs == [
        [Line(2, "call")],
        [Line(2, "call"), Line(3, "line")],
        [Line(2, "call"), Line(3, "line"), Line(3, "return")]
    ]
