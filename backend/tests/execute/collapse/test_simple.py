from cfg import ELLIPSE
from collapse import collapse
from helper import get_code_info
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

    graph = [8]
    code, lines, rest = collapse(graph, program_code, root)

    assert code == [
        "i = 1\n",
        "twos, fives = 0, 0\n",
        "while i < 6:\n",
        f"    {ELLIPSE}\n"
        "print(f\"2s: {twos}, 5s: {fives}\")\n"
    ]

    assert lines == [
        7, 
        8,
        9,
        None,
        24
    ]

    assert rest == [1]
