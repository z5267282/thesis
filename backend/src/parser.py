from collections import deque
import inspect
from typing import Deque, Type

from errors import UnsupportedIndentationError
import helper
from program import program
from tree import \
    CodeBlock, BodyBlock, BodyBlockDescendant, OptionalBodyBlock, \
    IfBlock, ElseBlock, ElifBlock, WhileBlock

def parse():
    lines, start = inspect.getsourcelines(program)
    # assume the first line is the function definition
    start += 1
    root : BodyBlock = BodyBlock(start)
    state : State = State(root)
    for line_no, line_contents in enumerate(lines, start=start):
        # print(f"{line_no}: {line}", end="")

        # ignore blank lines
        if all(l.isspace() for l in line_contents):
            continue

        line : str = helper.get_stripped_line(line_contents)
        # ignore comments
        if line.startswith("#"):
            continue

        leading_space : int = helper.num_leading_whitespace(line_contents)
        top           : BodyBlockDescendant = state.stack.peek()

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

            Conditional = IfBlock | ElifBlock | E
            unnested_block : IfBlock | WhileBlock | CodeBlock | Elif= CodeBlock(line_no)
            if line.startswith("if"):
                unnested_block = IfBlock(line_no)
            elif line.startswith("while"):
                unnested_block = WhileBlock(line_no)

            top : BodyBlockDescendant = state.stack.peek()
            top.add_same_level_block(unnested_block)
            state.stack.push(unnested_block) 

        # same level block
        else:
            pass
        
        # new block: how do you know the first time vs end of an existing block
        if state.indent_level is None:
            state.indent_level = leading_space
            state.start = line_no

class State:
    """a dataclass to store any necessary information during parsing
    used as the function to sys.settrace can only take in one helper argument"""
    def __init__(self, root : BodyBlock):
        self.indent_level : int = None
        self.start        : int = None
        self.end          : int = None
        self.filename     : str = inspect.getsourcefile(program)
        # the root must be a BodyBlock, because you don't know how to add nested blocks
        self.root         : BodyBlock = root
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

def init_root():
    # for now assume program is only top level code
    lines, start = inspect.getsourcelines(program)
    root = BodyBlock(start + 1)
    root.end = len(lines)
    return root

parse()
