def program():
    def f():
        print("a")
        print("b")
    
    print("start")
    f()

from tree import FunctionBlock
from tree_parser import parse

def test_name():
    root = parse(program)
    mapping = root.map_lines()
    func = mapping.get(2)
    assert func is not None
    assert isinstance(func, FunctionBlock)
    assert func.name == "f"
