def program():
    name = "Bob"
    money = 10
    print(f"{name} has {money} dollars")

from collections import OrderedDict

from analyse import smart_trace
from config import OFFSET
from collapse import collapse
from dataframe import DataFrame
from graph import generate_graphs
from helper import get_code_info, get_stripped_line
from line import Line
from evaluate import evaluate
from execute import trace_program
from state import State
from tree import Block, BodyBlock
from tree_parser import parse

def test_simple():
    root         = parse(program)

    l2           = Line(3, {})
    l2.vars.curr = {"name" : "Bob"}

    l4           = Line(4, {"name" : "Bob", "money" : 10})
    l4.vars.curr = l4.vars.prev
    l4.output = ["Bob has 10 dollars"]

    program_code = get_code_info(program)

    curr = 2
    evalbox = []
    code, lines, path = collapse([l2, l4], program_code, root)
    frame = DataFrame(
        code, lines,
        curr, l4.vars, l4.output,
        path, l4.counters, evalbox
    )

    assert frame.to_dict() == {
        "code"     : [
            "name = \"Bob\"",
            "money = 10",
            "print(f\"{name} has {money} dollars\")"
        ],
        "lines"    : [1, 2, 3],
        "curr"     : curr,
        "vars"     : [
            {
                "name"    : "name",
                "value"   : "Bob",
                "changed" : False
            },
            {
                "name"    : "money",
                "value"   : "10",
                "changed" : False
            }
        ],
        "out"      : l4.output,
        "path"     : path,
        "counters" : [],
        "evalbox"  : evalbox
    }
