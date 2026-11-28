def program():
    i = 0
    while i < 3:
        print("hello mate")
        i += 1

from analyse import smart_trace_all
from collapse import collapse
from counter import Counter
from execute import trace_program
from graph import generate_graphs
from helper import get_code_info
from line import Line
from tree_parser import parse

def test_while_counter():
    root = parse(program)
    line_mapping = root.map_lines()
    run_lines = trace_program(program)
    filtered, = smart_trace_all(line_mapping, run_lines)
    graphs = generate_graphs(filtered, line_mapping)
    program_code = get_code_info(program)

    assert graphs == [
        [Line(2)],
        [Line(2), Line(3)],
        [Line(2), Line(3), Line(5)],
        [Line(2), Line(3, event="return")]
    ]

    _, lines, _, _ = collapse(graphs[1], [], program_code, root)
    _, line = graphs[1]
    assert line.counters == [Counter(1, 3, line_mapping[3])]
    counter, = line.counters
    assert lines == [2, 3, None]
    assert counter.start == 1
    assert counter.end == 2
    assert counter.has_valid_range()

    _, lines, _, _ = collapse(graphs[2], [], program_code, root)
    _, _, line = graphs[2]
    assert line.counters == [Counter(1, 3, line_mapping[3])]
    counter, = line.counters
    assert lines == [2, 3, 4, 5]
    assert counter.start == 1
    assert counter.end == 3
