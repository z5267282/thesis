def program():
    def f():
        print("a")
        print("b")
    
    print("start")
    f()

from tree_parser import parse

def test_simple():
    root = parse(program)
    root.pretty_print()
    assert False
