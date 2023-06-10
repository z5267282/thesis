from collections import deque
import inspect
from typing import Callable, Deque, Type

import helper
from tree import \
    CodeBlock, BodyBlock, BodyBlockDescendant, OptionalBodyBlock, \
    IfBlock, ElseBlock, ElifBlock, ConditionalBlock, WhileBlock

def parse(program : Callable):
    lines, start = inspect.getsourcelines(program)
    # assume the first line is the function definition
    start += 1
    root  : BodyBlock = BodyBlock(start)
    state : State = State(root)
    for line_no, line_contents in enumerate(lines, start=start):
        line          : str = helper.get_stripped_line(line_contents)
        leading_space : int = helper.num_leading_whitespace(line_contents)
        top           : BodyBlockDescendant = state.stack.peek()
        # use indent_level to track whether the first line has been entered
        if state.indent_level is None:
            state.indent_level = leading_space
            first_block = parse_line(line, line_no)
            top.add_same_level_block(first_block)
            if isinstance(first_block, CodeBlock):
                # assign the end through the state
                state.stack.code_block = first_block
            else:
                state.stack.push(first_block)
        # found indented block
        # the current BodyBlock should not have ended
        if leading_space > state.indent_level:
            nested_block = parse_line(line, line_no)
            if isinstance(nested_block, CodeBlock):
                state.code_block = nested_block 
            else:
                top.add_same_level_block(nested_block)
                state.stack.push(nested_block) 
        # unindented block
        # an indented block has just ended
        elif leading_space < state.indent_level:
            prev : int = line_no - 1
            if state.code_block is not None:
                state.code_block.end = prev
                top.add_same_level_block(state.code_block)
                state.code_block = None
            top.end = prev
            state.stack.pop()
            unnested_block = parse_line(line, line_no)
            top = state.stack.peek()
            if isinstance(nested_block, CodeBlock):
                state.code_block = nested_block 
            else:
                top.add_same_level_block(unnested_block)
                state.stack.push(unnested_block) 
        # same level block
        else:
            # code block
            next_block = parse_line(line, line_no)
            if not isinstance(next_block, CodeBlock):
                prev : int = line_no - 1
                if state.code_block is not None:
                    state.code_block.end = prev
                    top.add_same_level_block(state.code_block)
                    state.code_block = None
                else:
                    # TODO
                    pass

            # or nested block
        state.indent_level = leading_space
    # TODO: last line

def parse_line(line : str, line_no : int):
    if line.startswith("if"):
        return IfBlock(line_no)
    if line.startswith("while"):
        return WhileBlock(line_no)
    if line.startswith("elif"):
        return ElifBlock(line_no)

    return CodeBlock(line_no)

class State:
    """a dataclass to store any necessary information during parsing
    used as the function to sys.settrace can only take in one helper argument"""
    def __init__(self, root : BodyBlock):
        self.indent_level : int = None
        # the current code block if any
        # these should never be on the stack
        self.code_block   : CodeBlock = None
        self.stack        : Stack = Stack(root)

class Stack:
    """a simple wrapper around deque"""
    def __init__(self, root : BodyBlock):
        self.items : Deque[BodyBlockDescendant] = deque()
        self.push(root)
    
    def __len__(self):
        return len(self.items)

    def push(self, item : OptionalBodyBlock):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        """method according to the documentation here:
        https://docs.python.org/3/library/collections.html#collections.deque"""
        return self.items[-1]

def init_root(program : Callable):
    # for now assume program is only top level code
    lines, start = inspect.getsourcelines(program)
    root = BodyBlock(start + 1)
    root.end = len(lines)
    return root
