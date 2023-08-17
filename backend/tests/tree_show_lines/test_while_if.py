from collections import OrderedDict

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

    seen = OrderedDict()
    for i in range(root.start, root.end + 1):
        seen[i] = False
    
    root.show_lines() 

