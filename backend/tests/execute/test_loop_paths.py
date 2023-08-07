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
        print("{}: {}".format(filtered[i].line_no, ", ".join(str(j) for j in filtered[i].loop_path)))

    # for clarity, let's write the line numbers as well

    # code region
    assert filtered[0].line_no == 7
    assert filtered[0].loop_path == []

    # while region
    assert filtered[1].line_no == 8
    assert filtered[1].loop_path == []

    assert filtered[2].line_no == 9
    assert filtered[2].loop_path == [8]
    assert filtered[3].loop_path == [8, 9]
    assert filtered[4].loop_path == [8, 9, 10]
    assert filtered[5].loop_path == [8, 9, 10, 12]

    # code block
    assert filtered[6].loop_path == []
