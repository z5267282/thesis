from copy import deepcopy

from typing import Type

from line import Line
from tree import Block, CodeBlock, IfBlock, ElifBlock, ElseBlock, WhileBlock

def smart_trace(line_mapping : dict[int, Type[Block]], lines : list[Line]):
    """From a list of raw Lines of execution, generate an intelligent
    filtering.
    Decompose lines into regions of CodeBlocks, IfBlocks or WhileBlocks."""
    filtered : list[Line] = []
    i        : int = 0
    while i < len(lines):
        # we assume that i is the start of a region
        line  : Line = lines[i]
        block : Type[Block] = line_mapping[line.line_no]
        region, offset = find_region(lines, block.end, i)
        if isinstance(block, CodeBlock):
            filtered.append(trace_code_block(region))
        elif isinstance(block, IfBlock):
            won, rest = trace_if(region, block)
            if won is not None:
                filtered.append(won)
                filtered.extend(smart_trace(line_mapping, rest))
        elif isinstance(block, WhileBlock): # pragma no branch
            raw  : list[list[Line]] = trace_while(region, block)
            seen : list[list[Line]] = []
            for r in raw:
                rest = smart_trace(line_mapping, r[1:])
                # use slice rather than r[0] to support list + operator
                path = r[:1] + rest
                if path not in seen:
                    filtered.extend(path)
                    seen.append(path)

        i = offset
    
    return filtered

def find_region(lines : list[Line], end : int, start : int):
    """Return a region and the next line in lines to go to"""
    region : list[Line] = []
    i      : int = start
    while i < len(lines) and lines[i].line_no <= end:
        region.append(lines[i])
        i += 1

    return region, i

def trace_code_block(lines: list[Line]):
    """Return the end of a CodeBlock"""
    last : Line = lines[-1]
    return last

def trace_if(lines: list[Line], root : IfBlock):
    """Given all lines related to an if statement, filter out the winning
    path.
    If no branch won, return None and an empty list.
    Otherwise, return the won branch and the remaining lines in the region to be
    parsed."""
    won              : Line | None = None
    last_seen_branch : IfBlock | ElifBlock | ElseBlock | None = None

    for i, line in enumerate(lines):
        line_no : int = line.line_no
        branch  : IfBlock | ElifBlock | ElseBlock | None = root.find_branch(
            line_no
        )
        if branch is not None:
            # elses do not have their lines executed;
            # instead make a copy of the last seen branch
            if isinstance(branch, ElseBlock):
                else_line : Line = deepcopy(won)
                else_line.line_no = branch.start
                return else_line, lines[i:]

            won = line
            last_seen_branch = branch
        elif (
            last_seen_branch is not None
            and line_no == last_seen_branch.get_top().start
        ):
            return won, lines[i:]

    return None, []

def trace_while(lines : list[Line], while_ : WhileBlock):
    """Filter out a sequence of while iterations into paths.
    Return the unique execution paths taken within the loop as a list of Lines.
    All lines in the path will have a counters added to them."""
    all_paths : list[list[Line]] = []
    curr      : list[Line] = []
    for line in lines:
        # start of new path
        # must make sure we're not on the first line of the whole while
        # this ensures the last check which fails the while is not run
        if line.line_no == while_.start and curr:
            all_paths.append(curr)
            curr = []

        curr.append(line)
    
    # should not filter any lines from a non-taken while
    if not all_paths:
        return all_paths
    
    paths : list[list[Line]] = []
    n     : int = len(all_paths)
    for i, path in enumerate(all_paths, start=1):
        # this relies on Line.__eq__ using the line number only
        if path not in paths:
            for line in path:
                line.add_counter(i, n, while_)

            paths.append(path)
    
    return paths
