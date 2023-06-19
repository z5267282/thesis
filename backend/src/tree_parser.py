from collections import deque
import inspect
from typing import Callable, Type

from errors import ElseParseError, ElifParseError, NoEnclosingIfError
import helper
from stack import Stack
from tree import \
    Block, CodeBlock, BodyBlock, IfBlock, ElseBlock, ElifBlock, WhileBlock

def parse(program : Callable):
    # assume the first line is the function definition
    OFFSET = 1

    lines, start = inspect.getsourcelines(program)
    start += OFFSET
    root        : BodyBlock = None
    stack       : Stack = None
    prev_indent : int = None
    line_no     : int = 0
    for line_no, line_contents in enumerate(lines[OFFSET:], start=start):
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

        top : Type[BodyBlock] = stack.peek()
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
            print(f"bigger line found: {line_no}")
            nested_block : Type[Block] = parse_line(line, line_no, indent_level)
            if isinstance(first_block, ElifBlock):
                raise ElifParseError
            if isinstance(first_block, ElseBlock):
                raise ElseParseError

            if isinstance(nested_block, CodeBlock):
                top.code_block = nested_block 
            elif isinstance(nested_block, (IfBlock, WhileBlock)):
                stack.push(nested_block) 
            top.add_same_level_block(nested_block)
        # unindented block
        elif indent_level < prev_indent:
            prev : int = line_no - 1
            if top.code_block is not None:
                top.code_block.end = prev
                top.code_block = None
            # pop off stack until same level block is found
            root.pretty_print()
            while top.indent_level != indent_level:
                top.end = prev
                stack.pop()
                top = stack.peek()
            unnested_block = parse_line(line, line_no, indent_level)
            if isinstance(unnested_block, CodeBlock):
                top.code_block = unnested_block 
            else:
                if isinstance(unnested_block, ElifBlock):
                    if not isinstance(top, IfBlock):
                        raise NoEnclosingIfError(True)
                    top.elifs.append(unnested_block)
                if isinstance(unnested_block, ElseBlock):
                    if not isinstance(top, IfBlock):
                        raise NoEnclosingIfError(False)
                    top.else_ = unnested_block
                stack.push(unnested_block)
            top.add_same_level_block(unnested_block)
        prev_indent = indent_level

        # print(f"line: {line_no}")
        # print(stack)
        # print("---")

    # last line
    last : int = start + len(lines) - 1 - OFFSET
    top  : Type[BodyBlock] = stack.peek()
    if top.code_block is not None:
        top.code_block.end = last
        top.code_block = None
    while not stack.empty():
        top = stack.peek() 
        top.end = last
        stack.pop()
    return root

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
