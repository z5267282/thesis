from config import ELLIPSE
from collapse import collapse
from helper import get_code_info
from line import Line
from tree_parser import parse

def program():
    i = 1
    if i % 2 == 0:
        print("two")
        twos += 1
    elif i % 5 == 0:
        print("five")
        fives += 1
    else:
        print("what a special character!")

    print(f"2s: {twos}, 5s: {fives}")

def test_if_elif():
    root = parse(program)
    program_code = get_code_info(program)

    graph = [Line(8, {}), Line(9, {}), Line(11, {}), Line(18, {})]
    code, lines, rest = collapse(graph, program_code, root)

    assert code == [
        "i = 1",
        "if i % 2 == 0:",
        "    print(\"two\")",
        "    twos += 1",
        "elif i % 5 == 0:",
        f"    {ELLIPSE}",
        "else:",
        f"    {ELLIPSE}",
        "print(f\"2s: {twos}, 5s: {fives}\")"
    ]

    assert lines == [
        8, 
        9,
        10,
        11,
        12,
        None,
        15,
        None,
        18 
    ]

    assert rest == [0, 1, 3, 8]
