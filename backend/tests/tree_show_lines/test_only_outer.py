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

def test_inner_show():
    root = parse(program)

    show = OrderedDict()
    for i in range(root.start, root.end + 1):
        show[i] = False
    
    graph = [7]
    root.show_lines(graph, show) 

    exp = OrderedDict()
    exp[6] = True
    exp[7] = True
    exp[8] = True
    exp[9] = False 
    exp[10] = False 
    exp[11] = False 
    exp[12] = False 
    exp[13] = False
    exp[14] = False
    # whitespace should be considered part of the line 12 elif
    exp[15] = False
    exp[16] = False 
    exp[17] = False 
    exp[18] = False 
    exp[19] = False 
    # whitespace should be part of the line 17 while
    exp[20] = False 
    exp[21] = False 
    exp[22] = False 
    exp[23] = True

    assert show == exp
