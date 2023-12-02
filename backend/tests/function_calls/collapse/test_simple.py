def program():
    def a():
        print("a")
    
    i = 0
    if i == 1:
        print("1")
    else:
        print("s")
        a() 

from collapse import collapse
from helper import get_code_info
from line import Line
from tree_parser import parse

def test_nested():
    """Check if collapse will show both the:
    1. current graph : function call
    2. the previous context : top-level conditional"""
    root = parse(program)
    code = get_code_info(program)
    collapse(
        [Line(2, "call"), Line(3, "line")],
        [Line(5, "line"), Line(8, "line"), Line(10, "line")],
        code, root
    )
