from cfg import ELLIPSE
from collapse import collapse
from helper import get_code_info
from line import Line
from tree_parser import parse

def program():
    i = 1
    twos, fives = 0, 0
    while i < 6:
        if i % 2 == 0:
            print("two")
            twos += 1
        elif i % 5 == 0:
            print("five")
            fives += 1

        j = 0
        while j < i:
            print("X", end="")
            j += 1

        i += 1

    print(f"2s: {twos}, 5s: {fives}")

def test_simple():
    root = parse(program)
    program_code = get_code_info(program)

    graph = [Line(9, {})]
    code, lines, rest = collapse(graph, program_code, root)

    assert code == [
        "i = 1",
        "twos, fives = 0, 0",
        "while i < 6:",
        f"    {ELLIPSE}",
        "print(f\"2s: {twos}, 5s: {fives}\")"
    ]

    assert lines == [
        8, 
        9,
        10,
        None,
        25
    ]

    assert rest == [1]
