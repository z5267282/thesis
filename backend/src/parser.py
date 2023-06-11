from collections import deque
import inspect
from typing import Callable, Deque, Type

from errors import ElseParseError, ElifParseError
import helper
from tree import \
    Block, CodeBlock, BodyBlock, OptionalBodyBlock, \
    IfBlock, ElseBlock, ElifBlock, ConditionalBlock, WhileBlock

def parse(program : Callable):
    lines, start = inspect.getsourcelines(program)
    # assume the first line is the function definition
    start += 1
    root        : BodyBlock = None
    stack       : Stack = None
    prev_indent : int = None
    line_no     : int = 0
    for line_no, line_contents in enumerate(lines, start=start):
        line        : str = helper.get_stripped_line(line_contents)
        indent_level : int = helper.num_leading_whitespace(line_contents)

        # first line
        if prev_indent is None:
            prev_indent = indent_level
            first_block : Type[Block] = parse_line(line, line_no, indent_level)
            if isinstance(first_block, ElifBlock):
                raise ElifParseError
            if isinstance(first_block, ElseBlock):
                raise ElseParseError

            root = BodyBlock(line_no, line_contents)
            stack = Stack(root)
            if isinstance(first_block, (IfBlock, WhileBlock)):
                stack.push(first_block)
            elif isinstance(first_block, CodeBlock):
                root.code_block = first_block
            root.add_same_level_block(first_block)
            continue

        top  : Type[BodyBlock] = stack.peek()
        if indent_level == prev_indent:
            level_block : Type[Block] = parse_line(line, line_no, indent_level)
            if isinstance(level_block, CodeBlock):
                # no need to set the indentation level if its the same
                continue
            if isinstance(level_block, ElifBlock):
                raise ElifParseError
            if isinstance(level_block, ElseBlock):
                raise ElseParseError

            if isinstance(level_block, (IfBlock, WhileBlock)):
                if top.code_block is not None:
                    prev : int = line_no - 1
                    top.code_block.end = prev
                    top.code_block = None
                top.add_same_level_block(level_block)
                stack.push(level_block)

        # indented block
        elif indent_level > prev_indent:
            nested_block : Type[Block] = parse_line(line, line_no, indent_level)
            if isinstance(first_block, ElifBlock):
                raise ElifParseError
            if isinstance(first_block, ElseBlock):
                raise ElseParseError

            if isinstance(nested_block, CodeBlock):
                top.code_block = nested_block 
            elif isinstance(first_block, (IfBlock, WhileBlock)):
                stack.push(nested_block) 
            top.add_same_level_block(nested_block)
        # unindented block
        elif indent_level < prev_indent:
            prev : int = line_no - 1
            if top.code_block is not None:
                top.code_block.end = prev
                top.code_block = None
            # pop off stack until same level block is found
            while top.indent_level != indent_level:
                top.end = prev
                stack.pop()
                top = stack.peek()
            unnested_block = parse_line(line, line_no, indent_level)
            if isinstance(unnested_block, CodeBlock):
                top.code_block = unnested_block 
            if isinstance(unnested_block, ElifBlock):
                # if 
                pass
            top.add_same_level_block(unnested_block)

        prev_indent = indent_level
    # TODO: last line

def parse_line(line : str, line_no : int, indent_level : int):
    if line.startswith("if"):
        return IfBlock(line_no, indent_level)
    if line.startswith("while"):
        return WhileBlock(line_no, indent_level)
    if line.startswith("elif"):
        return ElifBlock(line_no, indent_level)
    if line.startswith("else"):
        return ElseBlock(line_no, indent_level)
    return CodeBlock(line_no)

class Stack:
    """a simple wrapper around deque"""
    def __init__(self, root : BodyBlock):
        self.items : Deque[Type[BodyBlock]] = deque()
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
