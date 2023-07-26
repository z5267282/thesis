from typing import Callable, Type

from line import Line
from tree import Block, CodeBlock, IfBlock, ElifBlock, ElseBlock, WhileBlock

def smart_trace(line_mapping : dict[int, Type[Block]], lines : list[Line]):
    """From a list of raw Lines of execution, generate an intelligent
    filtering.
    Decompose lines into regions of CodeBlocks, IfBlocks or WhileBlocks."""
    filtered : list[Line] = []
    i : int = 0
    while i < len(lines):
        # we assume that i is the start of a region
        line  : Line = lines[i]
        block : Type[Block] = line_mapping[line.line_no]
        region, offset = find_region(lines, block.end, i)
        if isinstance(block, CodeBlock):
            filtered.extend(trace_code_block(region))
        elif isinstance(block, IfBlock):
            # TODO
            pass
        elif isinstance(block, WhileBlock):
            j = i
            while_lines : list[Line] = []
            while lines[j].line_no <= block.end:
                while_lines.append(j)
                j += 1
            lines.extend(trace_while(while_lines))

def find_region(lines : list[Line], end : int, start : int):
    """Return a region and the next line in lines to go to"""
    region : list[Line] = []
    i : int = start
    while i < len(lines) and lines[i].line_no <= end:
        region.append(lines[i])
        i += 1
    return region, i

def trace_code_block(region: list[Line]):
    last : Line = region[-1]
    return [last]

def find_last(lines : list[Line], end : int):
    last = None
    i = 0
    while list[i].line_no <= end:
        last = list[i]
        i += 1
    return last


def trace_if(line_mapping : dict[int, Type[Block]], lines: list[Line], root : IfBlock):
    """
        Given all lines related to an if statement, filter out the winning path
    """
    MaybeConditional = IfBlock | ElifBlock | ElseBlock | None 
    won : Line | None = None
    result : list[Line] = [] 

    i : int = 0
    while i < len(lines):
        line : Line = lines[i]
        line_no : int = line.line_no
        branch : MaybeConditional = root.find_branch(line_no)
        if branch is not None:
            won = line
        elif line_no == branch.get_top().start:
            result.append(won)
            result.extend(lines[i:])
            break
        i += 1
    
    return result
    #     # current line is more deeply nested than previous
    #     # cannot see indentation level of current line
    #     # blank lines -> cannot rely on this
    #     line_no = branch.line_no
    #     block = line_mapping[branch.line_no]

    #     # or, current line is the start of a branch's top

def trace_while(lines : list[Line]):
    # get first path
    i = 0
    # while 
    return []
