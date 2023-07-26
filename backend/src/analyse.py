from collections import OrderedDict
from fractions import Fraction
from typing import Type

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
            won, rest = trace_if(lines, block)
            filtered.append(won)
            filtered.extend(smart_trace(line_mapping, rest))
        elif isinstance(block, WhileBlock):
            j = i
            while_lines : list[Line] = []
            while lines[j].line_no <= block.end:
                while_lines.append(j)
                j += 1
            lines.extend(trace_while(while_lines))
        i = offset
    
    return filtered

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

def trace_if(lines: list[Line], root : IfBlock):
    """Given all lines related to an if statement, filter out the winning
    path.
    Return the won branch and the remaining lines in the region to be parsed."""
    won : Line | None = None
    rest : list[Line] = [] 

    i : int = 0
    while i < len(lines):
        line : Line = lines[i]
        line_no : int = line.line_no
        MaybeConditional = IfBlock | ElifBlock | ElseBlock | None 
        branch : MaybeConditional = root.find_branch(line_no)
        if branch is not None:
            won = line
        elif line_no == branch.get_top().start:
            rest.extend(lines[i:])
            break
        i += 1

    return won, rest

def trace_while(lines : list[Line], start : int):
    paths : list[Line] = []
    curr : list[Line] = []
    for i, line in enumerate(lines):
        # start of new path
        # must make sure we're not on the first line of the whole while
        if i == start and curr:
            paths.append(curr)
            curr.clear()

        curr.append(line)

    # should not filter any lines from a non-taken while
    if not paths:
        return []
    
    # last path will be just the while
    paths.pop(-1)
    result : OrderedDict[tuple[Line], Fraction] = OrderedDict()
    for i, path in enumerate(paths, start=1):
        tuple_path = tuple(path)
        if tuple_path not in result:
            # result[tuple_path] = 
