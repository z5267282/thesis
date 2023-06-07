import inspect
import linecache
import sys
from types import FrameType
from typing import Any

import helper
from parser import init_state, State
from program import program
from tree import BodyBlock, CodeBlock, WhileBlock, IfBlock

state : State = init_state()

def trace_execution(frame : FrameType, event : str, arg : Any):
    # only consider normal lines for now
    if event != "line":
        return trace_execution
    
    line_no = frame.f_lineno
    line_contents = linecache.getline(state.filename, line_no)
    leading_space = helper.num_leading_whitespace(line_contents)
    line = helper.get_stripped_line(line_contents)
    top : BodyBlock = state.stack.peek()

    if state.is_first:
        state.start = line_no
        state.indent_level = leading_space
        state.is_first = False
    # elif 

    # found indented block
    if leading_space > state.indent_level:
        # an indented if statement
        if line.startswith("if"):
            if_block = IfBlock(line_no)
            # top.add
        
    # new block: how do you know the first time vs end of an existing block
    if state.indent_level is None:
        state.indent_level = leading_space
        state.start = line_no

    print(f'{line_no:2} | {line_contents[:-1]}')
    return trace_execution

sys.settrace(trace_execution)
program()
