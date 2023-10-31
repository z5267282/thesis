def program():
    i = 0
    while i < 3:
        print(i)
        i += 1

from collapse import collapse
from config import ELLIPSE, LEADING_SPACES
from dataframe import DataFrame
from helper import get_code_info
from line import Line
from state import State
from tree_parser import parse

def test_first_line():
    root = parse(program)
    program_code = get_code_info(program)

    variables = {"i" : 0}
    curr = 1
    counters = []
    output, evalbox = [], ["while 1 < 3"]
    code, lines, path = collapse([Line(2, {}), Line(3, {})], program_code, root)
    frame = DataFrame(
        code, lines,
        curr, State(variables, curr=variables),
        output, path, counters, evalbox
    )
    assert frame.to_dict() == {
        "code"     : [
            "i = 0",
            "while i < 3:",
            "{}{}".format(" " * LEADING_SPACES, ELLIPSE)
        ],
        "lines"    : [2, 3, None],
        "curr"     : curr,
        "vars"     : [{"name" : "i", "value" : "0", "changed" : False}],
        "out"      : output,
        # this should now be changed to not include 0 as the start
        "path"     : {"start" : 0, "rest" : path[1:]},
        "counters" : counters,
        "evalbox"  : evalbox
    }
