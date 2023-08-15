import inspect
from typing import Callable, Type

from cfg import OFFSET
import helper
from stack import Stack
from tree import \
    Block, CodeBlock, BodyBlock, IfBlock, ElseBlock, ElifBlock, WhileBlock

def parse(program : Callable):
    lines, start = get_code_info(program)
    # the root and stack can only be initialised when the first line is parsed
    # however, their scope must cover the entire function
    # hence they are declared here
    root, stack, prev_indent, line_no = init_state()

    for line_no, line_contents in enumerate(lines[OFFSET:], start=start):
        line         : str = helper.get_stripped_line(line_contents)
        indent_level : int = helper.num_leading_whitespace(line_contents)

        # comment or blank line
        if is_skipable(line):
            continue

        # first line
        if prev_indent is None:
            prev_indent = indent_level
            root, stack = parse_first_line(line, line_no, indent_level)
            continue
        
        top   : Type[BodyBlock] = stack.peek()
        block : Type[Block] = parse_line(line, line_no, indent_level)
        if indent_level == prev_indent:
            parse_same_level_block(block, line_no, top, stack)
        elif indent_level > prev_indent:
            parse_indented_block(block, top, stack)
        else:
            parse_unindented_block(block, line_no, indent_level, top, stack)
        prev_indent = indent_level
    
    last : int = calculate_last_line(start, lines)
    parse_last_line(last, stack)
    return root

def get_code_info(program : Callable):
    lines, start = inspect.getsourcelines(program)
    start += OFFSET
    return lines, start

def init_state():
    root        : BodyBlock = None
    stack       : Stack[Type[BodyBlock]] = None
    prev_indent : int = None
    line_no     : int = 0
    return root, stack, prev_indent, line_no

def parse_first_line(line : str, line_no : int, indent_level : int):
    """Parse the first line in the program.
    Return the root of the tree and a stack with it."""
    first_block : Type[Block] = parse_line(line, line_no, indent_level)
    root = BodyBlock(line_no, indent_level)
    stack = Stack[BodyBlock](root)
    if isinstance(first_block, (IfBlock, WhileBlock)):
        stack.push(first_block)
    elif isinstance(first_block, CodeBlock): # pragma: no branch
        root.code_block = first_block
    # note we define it impossible to not start on an If, While or Code block
    root.add_same_level_block(first_block)
    return root, stack

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

def is_skipable(line : str):
    """check whether a line stripped of leading spaces is a comment or blank."""
    return line == "" or line.startswith("#")

def parse_same_level_block(
    block : Type[Block], line_no : int, top : Type[BodyBlock], stack : Stack[Type[BodyBlock]]
):
    if isinstance(block, CodeBlock):
        return

    # this is the only other option
    # but for clarity we define the condition
    if isinstance(block, (IfBlock, WhileBlock)): # pragma: no cover
        top.end_code_block(line_no - 1)
        top.add_same_level_block(block)
        stack.push(block)
    
    # impossible to get to this line

def parse_indented_block(
    block : Type[Block], top : Type[BodyBlock], stack : Stack[Type[BodyBlock]]
):
    handle_stack_indentation_change(block, top, stack)

def handle_stack_indentation_change(
    block : Type[Block], top : Type[BodyBlock], stack : Stack[Type[BodyBlock]]
):
    """Manage a new Block on the stack when indentation changes.
    Assume that if the Block introduces indentation it cannot be a branch
    (ie. not an Elif or an Else)."""
    if isinstance(block, CodeBlock):
        top.code_block = block 
    else:
        stack.push(block) 
    top.add_same_level_block(block)

def parse_unindented_block(
    block : Type[Block], line_no : int, indent_level : int,
    top : Type[BodyBlock], stack : Stack[Type[BodyBlock]],
):
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
    top : Type[BodyBlock], stack : Stack[Type[BodyBlock]],
    indent_level : int, prev : int
):
    """Pop off stack until a block with the same indentation level is found.
    Assume consistent indentation levels have been followed.
    In summary, ends all indents inside the current level.
    Return the new top."""
    while top.indent_level != indent_level:
        top.end = prev
        top = stack.pop_peek()
    return top

def is_branch(block : Type[BodyBlock]):
    """Check whether a BodyBlock is a branch of a parent if."""
    return isinstance(block, (ElifBlock, ElseBlock))

def add_branch(
    block : ElifBlock | ElseBlock, prev : int,
    top : Type[BodyBlock], stack : Stack[Type[BodyBlock]]
):
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
    prev : int, stack : Stack[Type[BodyBlock]]
):
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

def calculate_last_line(start : int, lines : list[str]):
    return start + len(lines) - 1 - OFFSET

def parse_last_line(last : int, stack : Stack[Type[BodyBlock]]):
    top : Type[BodyBlock] = stack.peek()
    top.end_code_block(last)
    while not stack.empty():
        top = stack.pop()
        top.end = last
