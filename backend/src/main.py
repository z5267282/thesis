import inspect
import linecache
import sys

import helper
from parse import State
from program import program

filename = inspect.getsourcefile(program)
lines = []
state = State()

def trace_execution(frame, event, arg):
    # only consider normal lines for now
    if event != "line":
        return trace_execution
    
    line_no = frame.f_lineno
    line_contents = linecache.getline(filename, line_no)
    leading_space = helper.num_leading_whitespace(line_contents)

    # first line

    # lazy technique
    # if all(attr is None for attr in [state.start, state.end]):
    if state.start is None and state.end is None:
        state.start = line_no
        state.indent_level = leading_space
    # end of a block
    elif state.start is None:
        

    # new block: how do you know the first time vs end of an existing block
    if state.indent_level is None:
        state.indent_level = leading_space
        state.start = line_no

    print(f'{line_no:2} | {line_contents[:-1]}')
    lines.append(line_no)

    return trace_execution

sys.settrace(trace_execution)
program()
