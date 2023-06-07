import inspect
import linecache
import sys
from types import FrameType
from typing import Any

from errors import UnsupportedIndentationError
import helper
from parser import init_state, State
from program import program
from tree import BodyBlock, BodyBlockDescendant, CodeBlock, ElifBlock, IfBlock, WhileBlock

state : State = init_state()

def trace_execution(frame : FrameType, event : str, arg : Any):
    # only consider normal lines for now
    if event != "line":
        return trace_execution
    
    line_no       : int = frame.f_lineno
    line_contents : str = linecache.getline(state.filename, line_no)
    # ignore blank lines
    if all(l.isspace() for l in line_contents):
        return trace_execution

    line          : int = helper.get_stripped_line(line_contents)
    # ignore comments
    if line.startswith("#"):
        return trace_execution

    leading_space : int = helper.num_leading_whitespace(line_contents)
    top : BodyBlockDescendant = state.stack.peek()

    # use indent_level to track whether the first line has been entered
    if state.indent_level is None:
        state.indent_level = leading_space

    # found indented block
    # the current BodyBlock should not have ended
    if leading_space > state.indent_level:
        nested_block : IfBlock | WhileBlock | None = None
        if line.startswith("if"):
            nested_block = IfBlock(line_no)
        elif line.startswith("while"):
            nested_block = WhileBlock(line_no)
        
        if nested_block is None:
            raise UnsupportedIndentationError
        
        top.add_same_level_block(nested_block)
        state.stack.push(nested_block) 
    # unindented block
    # an indented block has just ended
    elif leading_space < state.indent_level:
        top.end = line_no - 1
        state.stack.pop()

    # same level block
    else:
        pass
        
    # new block: how do you know the first time vs end of an existing block
    if state.indent_level is None:
        state.indent_level = leading_space
        state.start = line_no

    print(f'{line_no:2} | {line_contents[:-1]}')
    return trace_execution

sys.settrace(trace_execution)
program()
