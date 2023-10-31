def program():
    name = "Bob"
    money = 10
    print(f"{name} has {money} dollars")

from collapse import collapse
from dataframe import DataFrame
from helper import get_code_info
from line import Line
from state import State
from tree_parser import parse

def test_simple():
    root = parse(program)

    l4 = Line(4, {"name" : "Bob", "money" : 10})
    l4.output = ["Bob has 10 dollars"]

    program_code = get_code_info(program)

    curr = 2
    evalbox = []
    code, lines, path = collapse([l4], program_code, root)
    frame = DataFrame(
        code, lines,
        curr, State(l4.variables, curr=l4.variables), l4.output,
        path, l4.counters, evalbox
    )

    assert frame.to_dict() == {
        "code"     : [
            "name = \"Bob\"",
            "money = 10",
            "print(f\"{name} has {money} dollars\")"
        ],
        "lines"    : [2, 3, 4],
        "curr"     : curr,
        "vars"     : [
            {
                "name"    : "money",
                "value"   : "10",
                "changed" : False
            },
            {
                "name"    : "name",
                "value"   : "Bob",
                "changed" : False
            }
        ],
        "out"      : l4.output,
        "path"     : {"rest" : [2], "start" : 0},
        "counters" : [],
        "evalbox"  : evalbox
    }
