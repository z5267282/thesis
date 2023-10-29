def program():
    i = 0
    while i < 5:
        print(i)
        i += 1
    print("that's all folks")

from analyse import smart_trace
from collapse import collapse
from helper import get_code_info
from line import Line
from tree_parser import parse

def test_code_after():
    root = parse(program)
    line_mapping = root.map_lines()
    execution = [
        Line(2, {}),
        # loop iterations
        Line(3, {}), Line(4, {}), Line(5, {}),
        Line(3, {}), Line(4, {}), Line(5, {}),
        Line(3, {}), Line(4, {}), Line(5, {}),
        Line(3, {}), Line(4, {}), Line(5, {}),
        Line(3, {}), Line(4, {}), Line(5, {}),
        # breaking iteration
        Line(3, {}),
        Line(6, {})
    ]
    # should update the counters
    filtered = smart_trace(line_mapping, execution)
    assert filtered == [
        Line(2, {}),
        Line(3, {}), Line(5, {}),
        Line(6, {})
    ]

    program_code = get_code_info(program)
    # use the graph up to body of loop
    body_graph = filtered[:-1]
    collapse(body_graph, program_code, root)
    # counters now should have been updated
    _, condition, body, after_loop = filtered 

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

    assert not after_loop.counters
