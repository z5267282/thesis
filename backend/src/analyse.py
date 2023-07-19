from typing import Type

from line import Line
from tree import Block, CodeBlock, IfBlock, WhileBlock

def smart_trace(line_mapping : dict[int, Type[Block]], lines : list[Line]):
    """From a list of raw Lines of execution, generate an intelligent
    filtering"""
    filtered : list[Line] = []
    i = 0
    while i < len(lines):
        line  : Line = lines[i]
        block : Type[Block] = line_mapping[line.line_no]
        if isinstance(block, CodeBlock):
            filtered.append(line)
            j = i
            # find the end of the block
            while lines[j].line_no < block.end:
                j += 1
            filtered.append(lines[j])
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

def trace_if(lines: list[Line], root : IfBlock):


def trace_while(lines : list[Line]):
    # get first path
    i = 0
    # while 
    return []
