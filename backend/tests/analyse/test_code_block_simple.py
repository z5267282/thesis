from analyse import smart_trace
from line import Line
from tree_parser import parse

def program():
    print("hello!")
    print("what a wonderful day it is")
    city = "Sydney"
    print(f"in {city}!")

def test_code_block_simple():
    root = parse(program)
    line_mapping = root.map_lines()

    l1 = Line(6)
    l1.variables = {}
    l1.output = ["hello"]

    l2 = Line(7)
    l2.variables = {}
    l2.output = ["hello", "what a wonderful day it is"]

    l3 = Line(8)
    l3.variables = {"city": "Sydney"}
    l3.output = ["hello", "what a wonderful day it is"]
    
    l4 = Line(9, {"city": "Sydney"})
    l4.variables = {"city": "Sydney"}
    l4.output = ["hello", "what a wonderful day it is", "in Sydney"]

    lines = [l1, l2, l3, l4]

    assert smart_trace(line_mapping, lines) == [l4]
