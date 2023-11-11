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
        j = 0
        while j < 3:
            print("X", end="")
            j += 1
        i += 1

def test_while_2d_counter():
    root = parse(program)
    line_mapping = root.map_lines()
    run_lines, _ = trace_program(program)
    filtered = smart_trace(line_mapping, run_lines)
    graphs = generate_graphs(filtered, line_mapping)
    program_code = get_code_info(program)

    assert graphs == [
        [Line(11)],
        [Line(11), Line(12)],
        [Line(11), Line(12), Line(13)],
        [Line(11), Line(12), Line(13), Line(14)],
        [Line(11), Line(12), Line(13), Line(14), Line(16)],
        [Line(11), Line(12), Line(13), Line(17)],
    ]

    _, _, _, _, graph, _ = graphs
    _, lines, _ = collapse(graph, program_code, root)
    _, _, _, _, line = graph
    assert line.counters == [
        Counter(1, 3, line_mapping[12]), Counter(1, 3, line_mapping[14])

    ]
    outer, inner = line.counters
    assert lines == [11, 12, 13, 14, 15, 16, 17]

    assert outer.start == 1
    assert outer.end == 6

    assert inner.start == 3
    assert inner.end == 5

def test_nested_loop():
    root = parse(program)
    line_mapping = root.map_lines()
    run_lines, _ = trace_program(program)
    filtered = smart_trace(line_mapping, run_lines)
    graphs = generate_graphs(filtered, line_mapping)
    program_code = get_code_info(program)

    assert graphs == [
        [Line(11)],
        [Line(11), Line(12)],
        [Line(11), Line(12), Line(13)],
        [Line(11), Line(12), Line(13), Line(14)],
        [Line(11), Line(12), Line(13), Line(14), Line(16)],
        [Line(11), Line(12), Line(13), Line(17)],
    ]

    _, _, _, _, graph, _ = graphs
    _, lines, _ = collapse(graph, program_code, root)
    _, _, _, _, line = graph
    assert line.counters == [
        Counter(1, 3, line_mapping[12]), Counter(1, 3, line_mapping[14])

    ]
    outer, inner = line.counters
    assert lines == [11, 12, 13, 14, 15, 16, 17]

    assert outer.start == 1
    assert outer.end == 6

    assert inner.start == 3
    assert inner.end == 5

def test_collapsed_inner_loop():
    root = parse(program)
    line_mapping = root.map_lines()
    run_lines, _ = trace_program(program)
    filtered = smart_trace(line_mapping, run_lines)
    graphs = generate_graphs(filtered, line_mapping)
    program_code = get_code_info(program)

    assert graphs == [
        [Line(11)],
        [Line(11), Line(12)],
        [Line(11), Line(12), Line(13)],
        [Line(11), Line(12), Line(13), Line(14)],
        [Line(11), Line(12), Line(13), Line(14), Line(16)],
        [Line(11), Line(12), Line(13), Line(17)],
    ]

    _, _, _, _, _, graph = graphs
    _, lines, _ = collapse(graph, program_code, root)
    _, _, _, line = graph
    assert line.counters == [Counter(1, 3, line_mapping[12])]
    counter, = line.counters
    assert lines == [11, 12, 13, 14, None, 17]

    assert counter.start == 1
    assert counter.end == 5
