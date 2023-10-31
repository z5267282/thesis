def program():
    i = 0
    while i < 5:
        print(i)
        i += 1

from analyse import smart_trace
from collapse import collapse
from helper import get_code_info
from line import Line
from tree_parser import parse

def test_1d_loop():
    root = parse(program)
    line_mapping = root.map_lines()
    execution = [
        Line(2),
        # loop iterations
        Line(3), Line(4), Line(5),
        Line(3), Line(4), Line(5),
        Line(3), Line(4), Line(5),
        Line(3), Line(4), Line(5),
        Line(3), Line(4), Line(5),
        # breaking iteration
        Line(3)
    ]
    # should update the counters
    filtered = smart_trace(line_mapping, execution)
    assert filtered == [
        Line(2),
        Line(3), Line(5)
    ]

    # no counters should be valid for now
    _, condition, body = filtered

    assert len(condition.counters) == 1
    counter, = condition.counters
    assert not counter.has_valid_range()

    assert len(body.counters) == 1
    counter, = body.counters
    assert not counter.has_valid_range()

    program_code = get_code_info(program)
    # the graph corresponding to running the last body statement should be the
    # filtered graph, since we executed the entire program
    body_graph = filtered
    collapse(body_graph, program_code, root)
    # counters now should have been updated
    _, condition, body = body_graph 

    # both counters should now be the end of the body
    assert len(condition.counters) == 1
    counter, = condition.counters
    assert counter.has_valid_range()
    assert counter.start == 1
    assert counter.end == 3

    assert len(body.counters) == 1
    counter, = body.counters
    assert counter.has_valid_range()
    assert counter.start == 1
    assert counter.end == 3
