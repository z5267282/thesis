def program():
    name = "Bob"
    money = 10
    print(f"{name} has {money} dollars")

from collapse import collapse
from dataframe import DataFrame
from helper import get_code_info
from line import Line
from tree_parser import parse

def test_to_dicts():
    root         = parse(program)

    l4           = Line(4, {"name" : "Bob", "money" : 10})
    l4.vars.curr = l4.vars.prev
    l4.output = ["Bob has 10 dollars"]

    program_code = get_code_info(program)

    curr = 2
    evalbox = []
    code, lines, path = collapse([l4], program_code, root)
    frame = DataFrame(
        code, lines,
        curr, l4.vars, l4.output,
        path, l4.counters, evalbox
    )

    frames = DataFrame.to_dicts([frame])
    assert frames == [
        {
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
    ]