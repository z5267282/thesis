from collections import OrderedDict
from typing import Callable, Type

import helper
from stack import Stack
from tree import \
    Block, CodeBlock, BodyBlock, IfBlock, ElseBlock, ElifBlock, WhileBlock

from typing import Iterator

def parse(program : Callable) -> BodyBlock:
    raw_code = helper.get_code_info(program)
    code = iter(raw_code.items())
    stack : Stack[BodyBlock] = Stack()

    root, prev_indent = iterate_until_and_parse_first_line(code, stack)

    for line_no, line_contents in code:
        line = helper.get_stripped_line(line_contents)
        indent_level = helper.num_leading_whitespace(line_contents)

        if is_skipable(line):
            continue

        top = stack.peek()
        block = parse_line(line, line_no, indent_level)
        if indent_level == prev_indent:
            parse_same_level_block(block, line_no, top, stack)
        elif indent_level > prev_indent:
            parse_indented_block(block, top, stack)
        else:
            parse_unindented_block(block, line_no, indent_level, top, stack)
        prev_indent = indent_level
    
    last : int = calculate_last_line(raw_code)
    parse_last_line(last, stack)
    return root


def iterate_until_and_parse_first_line(code:Iterator[tuple[int, str]], stack : Stack[BodyBlock]) -> tuple[BodyBlock, int]:
    """Takes the given code and iterates until the first line. Return the root 
    BodyBlock and the first previous indentation value."""
    for line_no, line_contents in code:
        line = helper.get_stripped_line(line_contents)
        indent_level = helper.num_leading_whitespace(line_contents)

        if is_skipable(line):
            continue

        # now we have reached the first line
        prev_indent = indent_level
        root = parse_first_line(line, line_no, indent_level, stack)
        return root, prev_indent
    
    # this is a sign we could not run anything in the program
    # i.e. it was all comments, or it was empty
    raise NoCodeRunInProgramError()

class NoCodeRunInProgramError(Exception):
    def __init__(self):
        super().__init__()
    
    def __str__(self) -> str:
        return f"there was no runnable code in the program"

def parse_first_line(
    line : str, line_no : int, indent_level : int, stack : Stack[BodyBlock]
) -> BodyBlock:
    """Parse the first line in the program.
    Return the root of the tree and a stack with it."""
    first_block : Block = parse_line(line, line_no, indent_level)
    root        : BodyBlock = BodyBlock(line_no, indent_level)
    stack.push(root)
    if isinstance(first_block, (IfBlock, WhileBlock)):
        stack.push(first_block)
    elif isinstance(first_block, CodeBlock): # pragma: no branch
        root.code_block = first_block
    # note we define it impossible to not start on an If, While or Code block
    root.add_same_level_block(first_block)
    return root

def parse_line(line : str, line_no : int, indent_level : int) -> CodeBlock | BodyBlock:
    if line.startswith("if"):
        return IfBlock(line_no, indent_level)
    if line.startswith("while"):
        return WhileBlock(line_no, indent_level)
    if line.startswith("elif"):
        return ElifBlock(line_no, indent_level)
    if line.startswith("else"):
        return ElseBlock(line_no, indent_level)
    return CodeBlock(line_no, indent_level)

def is_skipable(line : str) -> bool:
    """check whether a line stripped of leading spaces is a comment or blank."""
    return line == "" or line.startswith("#")

def parse_same_level_block(
    block : CodeBlock | BodyBlock, line_no : int, top : BodyBlock,
    stack : Stack[BodyBlock]
) -> None:
    if isinstance(block, CodeBlock):
        return

    # this is the only other option
    # but for clarity we define the condition
    if isinstance(block, (IfBlock, WhileBlock)): # pragma: no branch
        top.end_code_block(line_no - 1)
        top.add_same_level_block(block)
        stack.push(block)
    
    # impossible to get to this line

def parse_indented_block(
    block : CodeBlock | BodyBlock, top : BodyBlock, stack : Stack[BodyBlock]
) -> None:
    handle_stack_indentation_change(block, top, stack)

def handle_stack_indentation_change(
    block : CodeBlock | BodyBlock, top : BodyBlock, stack : Stack[BodyBlock]
) -> None:
    """Manage a new Block on the stack when indentation changes.
    Assume that if the Block introduces indentation it cannot be a branch
    (ie. not an Elif or an Else)."""
    if isinstance(block, CodeBlock):
        top.code_block = block 
    else:
        stack.push(block) 
    top.add_same_level_block(block)

def parse_unindented_block(
    block : CodeBlock | BodyBlock, line_no : int, indent_level : int,
    top : BodyBlock, stack : Stack[BodyBlock],
) -> None:
    prev : int = line_no - 1
    top.end_code_block(prev)
    top = unwind_indentations(top, stack, indent_level, prev)

    if is_branch(block):
        add_branch(block, prev, top, stack)
    else:
        top_is_branch : bool = is_branch(top)
        if isinstance(top, IfBlock) or top_is_branch:
            top = end_conditional(top, top_is_branch, prev, stack)
        # this is the only other choice
        # we write the condition for clarity
        elif isinstance(top, WhileBlock): # pragma: no cover
            top.end = prev
            top = stack.pop_peek()
        handle_stack_indentation_change(block, top, stack)

def unwind_indentations(
    top : BodyBlock, stack : Stack[BodyBlock],
    indent_level : int, prev : int
) -> BodyBlock:
    """Pop off stack until a block with the same indentation level is found.
    Assume consistent indentation levels have been followed.
    In summary, ends all indents inside the current level.
    Return the new top."""
    while top.indent_level != indent_level:
        top.end = prev
        top = stack.pop_peek()
    return top

def is_branch(block : BodyBlock) -> bool:
    """Check whether a BodyBlock is a branch of a parent if."""
    return isinstance(block, (ElifBlock, ElseBlock))

def add_branch(
    block : ElifBlock | ElseBlock, prev : int,
    top : BodyBlock, stack : Stack[BodyBlock]
) -> None:
    """Add an elif or else to a parent if branch.
    The parent if will either be the first or second thing on the stack."""
    if isinstance(top, ElifBlock):
        top.end_code_block(prev)
        top.end = prev
        top = stack.pop_peek()
    add_branch : Callable = \
        top.add_elif if isinstance(block, ElifBlock) else top.add_else
    add_branch(block)
    stack.push(block)

def end_conditional(
    top : IfBlock | ElifBlock | ElseBlock, top_is_branch : bool,
    prev : int, stack : Stack[BodyBlock]
) -> IfBlock | ElifBlock | ElseBlock:
    """End an entire parent if block stored near the top of the stack.
    Return the new root.
    """
    # the top of the stack represents the last branch
    # if: there was only 1 branch
    # elif | else: there were at least 2 branches
    # in either case we need to end the last branch first
    top.end_code_block(prev)
    top.end = prev
    top = stack.pop_peek()
    # if the top was an elif or else, then the entire conditional must be ended
    if top_is_branch:
        top.end = prev
        top = stack.pop_peek()
    # there were reference issues when the top wasn't being returned
    return top

def calculate_last_line(code : OrderedDict[int, str]) -> int:
    return next(reversed(code))

def parse_last_line(last : int, stack : Stack[BodyBlock]) -> None:
    top : BodyBlock = stack.peek()
    top.end_code_block(last)
    while not stack.empty():
        top = stack.pop()
        top.end = last
