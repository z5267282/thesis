import inspect
from typing import Callable, Type

from cfg import OFFSET
from errors import ExpectedIfBlock
import helper
from stack import Stack
from tree import \
    Block, CodeBlock, BodyBlock, IfBlock, ElseBlock, ElifBlock, WhileBlock

def parse(program : Callable):
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

            if isinstance(nested_block, CodeBlock):
                top.code_block = nested_block 
            elif isinstance(nested_block, (IfBlock, WhileBlock)):
                stack.push(nested_block) 
            top.add_same_level_block(nested_block)
        # unindented block
        elif indent_level < prev_indent:
            if line_no == 15:
                print("here")
            prev : int = line_no - 1
            if top.code_block is not None:
                top.code_block.end = prev
                top.code_block = None
            # pop off stack until same level block
            # assumes consistent indentation levels have been followed
            # basically ends all indents inside the current level
            while top.indent_level != indent_level:
                top.end = prev
                stack.pop()
                top = stack.peek()

            unnested_block = parse_line(line, line_no, indent_level)

            is_elif : bool = isinstance(unnested_block, ElifBlock)
            if is_elif or isinstance(unnested_block, ElseBlock):
                # the top will either be the if, or an elif
                # if not, the top elif has ended
                if isinstance(top, ElifBlock):
                    top.end_code_block(prev)
                    top.end = prev
                    stack.pop()
                    top = stack.peek()
                add_branch : Callable = \
                    top.add_elif if is_elif else top.add_else
                add_branch(unnested_block)
                stack.push(unnested_block)
            else:
                # must end the current if branch if any
                is_el_block : bool = isinstance(top, (ElifBlock, ElseBlock))
                if isinstance(top, IfBlock) or is_el_block:
                    top.end_code_block(prev)
                    top.end = prev
                    stack.pop()
                    top = stack.peek()
                    # end the entire if block now
                    if is_el_block:
                        if not isinstance(top, IfBlock):
                            raise ExpectedIfBlock
                        top.end = prev
                        stack.pop()
                        top = stack.peek()
                elif isinstance(top, WhileBlock):
                    # a while by this point should have had its code block ended
                    top.end = prev
                    stack.pop()
                    top = stack.peek()

                # now handle the stack
                if isinstance(unnested_block, CodeBlock):
                    top.code_block = unnested_block 
                else:
                    stack.push(unnested_block)
                top.add_same_level_block(unnested_block)
        prev_indent = indent_level

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
