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
