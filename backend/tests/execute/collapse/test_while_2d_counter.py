def program():
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            print("X", end="")
            j += 1
        i += 1

from analyse import smart_trace_all
from collapse import collapse
from counter import Counter
from execute import trace_program
from graph import generate_graphs
from helper import get_code_info
from line import Line
from tree_parser import parse

def test_while_2d_counter():
    root = parse(program)
    line_mapping = root.map_lines()
    run_lines = trace_program(program)
    filtered, = smart_trace_all(line_mapping, run_lines)
    graphs = generate_graphs(filtered, line_mapping)
    program_code = get_code_info(program)

    assert graphs == [
        [Line(2)],
        [Line(2), Line(3)],
        [Line(2), Line(3), Line(4)],
        [Line(2), Line(3), Line(4), Line(5)],
        [Line(2), Line(3), Line(4), Line(5), Line(7)],
        [Line(2), Line(3), Line(4), Line(8)],
        [Line(2), Line(3, event="return")]
    ]

    _, _, _, _, graph, _, _ = graphs
    _, lines, _, _ = collapse(graph, [], program_code, root)
    _, _, _, _, line = graph
    assert line.counters == [
        Counter(1, 3, line_mapping[3]), Counter(1, 3, line_mapping[5])

    ]
    outer, inner = line.counters
    assert lines == [2, 3, 4, 5, 6, 7, 8]

    assert outer.start == 1
    assert outer.end == 6

    assert inner.start == 3
    assert inner.end == 5

def test_nested_loop():
    root = parse(program)
    line_mapping = root.map_lines()
    run_lines = trace_program(program)
    filtered, = smart_trace_all(line_mapping, run_lines)
    graphs = generate_graphs(filtered, line_mapping)
    program_code = get_code_info(program)

    assert graphs == [
        [Line(2)],
        [Line(2), Line(3)],
        [Line(2), Line(3), Line(4)],
        [Line(2), Line(3), Line(4), Line(5)],
        [Line(2), Line(3), Line(4), Line(5), Line(7)],
        [Line(2), Line(3), Line(4), Line(8)],
        [Line(2), Line(3, event="return")]
    ]

    _, _, _, _, graph, _, _ = graphs
    _, lines, _, _ = collapse(graph, [], program_code, root)
    _, _, _, _, line = graph
    assert line.counters == [
        Counter(1, 3, line_mapping[3]), Counter(1, 3, line_mapping[5])

    ]
    outer, inner = line.counters
    assert lines == [2, 3, 4, 5, 6, 7, 8]

    assert outer.start == 1
    assert outer.end == 6

    assert inner.start == 3
    assert inner.end == 5

def test_collapsed_inner_loop():
    root = parse(program)
    line_mapping = root.map_lines()
    run_lines = trace_program(program)
    filtered, = smart_trace_all(line_mapping, run_lines)
    graphs = generate_graphs(filtered, line_mapping)
    program_code = get_code_info(program)

    assert graphs == [
        [Line(2)],
        [Line(2), Line(3)],
        [Line(2), Line(3), Line(4)],
        [Line(2), Line(3), Line(4), Line(5)],
        [Line(2), Line(3), Line(4), Line(5), Line(7)],
        [Line(2), Line(3), Line(4), Line(8)],
        [Line(2), Line(3, event="return")]
    ]

    _, _, _, _, _, graph, _ = graphs
    _, lines, _, _ = collapse(graph, [], program_code, root)
    _, _, _, line = graph
    assert line.counters == [Counter(1, 3, line_mapping[3])]
    counter, = line.counters
    assert lines == [2, 3, 4, 5, None, 8]

    assert counter.start == 1
    assert counter.end == 5
