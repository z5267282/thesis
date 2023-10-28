def program():
    name = "Bob"
    money = 10
    print(f"{name} has {money} dollars")

from collapse import collapse
from dataframe import DataFrame
from helper import get_code_info
from state import State
from tree_parser import parse

def test_collapsed():
    root         = parse(program)
    program_code = get_code_info(program)

    curr = None
    evalbox = []
    code, lines, path = collapse([], program_code, root)
    frame = DataFrame(
        code, lines,
        curr, State({}, curr={}), [],
        path, [], evalbox
    )

    assert frame.to_dict() == {
        "code"     : [
            "name = \"Bob\"",
            "money = 10",
            "print(f\"{name} has {money} dollars\")"
        ],
        "lines"    : [2, 3, 4],
        "curr"     : curr,
        "vars"     : [],
        "out"      : [],
        "path"     : {"rest" : [], "start" : 0},
        "counters" : [],
        "evalbox"  : evalbox
    }
