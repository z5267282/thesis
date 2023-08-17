from cfg import ELLIPSE
from collapse import collapse
from helper import get_code_info
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

def test_graph_simple():
    root = parse(program)
    program_code = get_code_info(program)

    graph = [7, 8, 10, 17]
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
        7, 
        8,
        9,
        10,
        11,
        None,
        14,
        None,
        17 
    ]

    assert rest == [0, 1, 3, 8]
