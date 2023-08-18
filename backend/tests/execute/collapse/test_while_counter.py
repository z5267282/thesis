from analyse import smart_trace
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
        [Line(11, {})],
        [Line(11, {}), Line(12, {})],
        [Line(11, {}), Line(12, {}), Line(14, {})]
    ]

    _, lines, _ = collapse(graphs[1], program_code, root)
    _, line = graphs[1]
    assert line.counters == [Counter(1, 3, line_mapping[12])]
    counter, = line.counters
    assert lines == [11, 12, None]
    assert counter.start is None
    assert counter.end is None

    _, lines, _ = collapse(graphs[2], program_code, root)
    _, _, line = graphs[2]
    assert line.counters == [Counter(1, 3, line_mapping[13])]
    counter, = line.counters
    assert lines == [11, 12, 13, 14]
    assert counter.start == 1
    assert counter.end == 3
