import inspect
import linecache
import sys

import helper
from program import program

filename = inspect.getsourcefile(program)
lines = []

class State:
    def __init__(self):
        self.indent_level = None

state = State()

def trace_execution(frame, event, arg):
    # only consider normal lines for now
    if event != "line":
        return trace_execution
    
    line_no = frame.f_lineno
    line_contents = linecache.getline(filename, line_no)
    leading_space = helper.num_leading_whitespace(line_contents)

    # first line
    if state.indent_level is None:
        state.indent_level = leading_space

    print(f'{line_no:2} | {line_contents[:-1]}')
    lines.append(line_no)

    return trace_execution

sys.settrace(trace_execution)

program()
