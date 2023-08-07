from analyse import smart_trace
from execute import trace_program
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
        print("")
    print("done")

def test_no_gaps_2d_while():
    root = parse(program)
    line_mapping = root.map_lines()
    lines = trace_program(program)
    filtered = smart_trace(line_mapping, lines)

    for i in range(1, 6):
        print("{}({}): {}".format(i, lines[i].line_no, ", ".join(str(j) for j in lines[i].loop_path)))

    print(f"fish: {lines[4].line_no}")

    assert filtered == [
        Line(7, {}),
        Line(8, {}),
        Line(9, {}),
        Line(10, {}),
        Line(12, {}),
        Line(14, {}),
        Line(15, {})
    ]

    assert filtered[4].line_no == 11

    # code region
    assert filtered[0].loop_path == []

    # while region
    assert filtered[1].loop_path == []
    assert filtered[2].loop_path == [2]
    assert filtered[3].loop_path == [2, 3]
    assert filtered[4].loop_path == [2, 3, 4]
    assert filtered[5].loop_path == [2, 3, 4, 6]

    # code block
    assert filtered[6].loop_path == []
