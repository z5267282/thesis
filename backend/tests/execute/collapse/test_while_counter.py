from analyse import smart_trace
from cfg import ELLIPSE
from collapse import collapse
from counter import Counter
from execute import trace_program
from graph import generate_graphs
from helper import get_code_info
from line import Line
from tree_parser import parse

def program():
    i = 0
    while i < 3:
        print("hello mate")
        i += 1

def test_while_counter():
    root = parse(program)
    line_mapping = root.map_lines()
    run_lines = trace_program(program)
    filtered = smart_trace(line_mapping, run_lines)
    graphs = generate_graphs(filtered, line_mapping)
    program_code = get_code_info(program)

    assert graphs == [
        [Line(12, {})],
        [Line(12, {}), Line(13, {})],
        [Line(12, {}), Line(13, {}), Line(15, {})]
    ]

    _, line = graphs[1]
    assert line.counters == [Counter(1, 3, line_mapping[13])]
    counter, = line.counters
    _, lines, _ = collapse(graphs[1], program_code, root)
    assert lines == [12, 13, None]
    assert counter.start == 1
    assert counter.end == 1
