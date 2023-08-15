from typing import Type

from line import Line
from stack import Stack
from tree import Block, WhileBlock

def generate_graphs(
    filtered : list[Line], line_mapping : dict[int, Type[Block]]
):
    top_level : list[int] = []
    whiles    : Stack[While] = Stack[While]()
    return [
        generate_ith_graph(
            f.line_no, line_mapping[f.line_no], top_level, whiles
        ) for f in filtered
    ]

class While:
    def __init__(self, node : WhileBlock):
        self.node  : WhileBlock = node
        self.lines : list[int] = []

def generate_ith_graph(
    line_no : int, node : Type[Block],
    top_level : list[int], whiles : Stack[While]
):
    """Generate the execution graph up to the ith line.
    Return a list of raw line numbers to show in the graph."""
    result = lambda: generate_from_state(top_level, whiles)

    while whiles:
        top : While = whiles.peek()
        curr : WhileBlock = top.node
        if line_no == curr.start:
            top.lines.clear()
            return result()

        if line_no <= curr.end:
            break
    
    # the top of the stack now stores the correct item
    if isinstance(node, WhileBlock):
        whiles.push(While(node))
    elif whiles:
        top : While = whiles.peek()
        top.lines.append(line_no)
    else:
        top_level.append(line_no)
    return result()

def generate_from_state(top_level : list[int], whiles : Stack[While]):
    result : list[int] = top_level.copy()
    # stack supports linear iteration from bottom to top
    for w in whiles:
        result.append(w.node.start)
        result.extend(w.lines)
    return result
