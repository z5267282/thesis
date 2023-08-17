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

def test_graph_simple():
    root = parse(program)
    program_code = get_code_info(program)
    graph = [
        Line(9, {}),
        Line(10, {}),
        Line(14, {}),
        Line(16, {}),
        Line(18, {}),
        Line(19, {}),
        Line(21, {})
    ]
    code, lines, rest = collapse(graph, program_code, root)

    assert code == [
        "i = 1",
        "twos, fives = 0, 0",
        "while i < 6:",
        "    if i % 2 == 0:",
        f"        {ELLIPSE}",
        "    elif i % 5 == 0:",
        "        print(\"five\")",
        "        fives += 1",
        "",
        "    j = 0",
        "    while j < i:",
        "        print(\"X\", end=\"\")",
        "        j += 1",
        "",
        "    i += 1",
        "",
        "print(f\"2s: {twos}, 5s: {fives}\")"
    ]

    assert lines == [
        8,
        9,
        10,
        11,
        None,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
    ]

    assert rest == [1, 2, 5, 7, 9, 10, 12]
