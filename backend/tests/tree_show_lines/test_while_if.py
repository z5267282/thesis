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

    show = OrderedDict()
    for i in range(root.start, root.end + 1):
        show[i] = False
    
    graph = [7, 8, 9, 11, 16, 17, 19]
    root.show_lines(graph, show) 

    exp = OrderedDict()
    exp[6] = True
    exp[7] = True
    exp[8] = True
    exp[9] = True
    exp[10] = True
    exp[11] = True
    exp[12] = True
    exp[13] = False
    exp[14] = False
    # whitespace should be considered part of the line 12 elif
    exp[15] = False
    exp[16] = True
    exp[17] = True
    exp[18] = True
    exp[19] = True
    # whitespace should be part of the line 17 while
    exp[20] = True
    exp[21] = True
    exp[22] = True
    exp[23] = True

    assert show == exp
