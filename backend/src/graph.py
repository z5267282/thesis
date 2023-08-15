from collections import namedtuple
from typing import Type

from stack import Stack
from tree import Block, BodyBlock, WhileBlock

class While:
    def __init__(self, node : WhileBlock):
        self.node  : WhileBlock = node
        self.lines : list[int] = []
    
def generate_from_state(top_level : list[int], whiles : Stack[While]):
    result : list[int] = list.copy()
    # stack supports linear iteration from bottom to top
    for w in whiles:
        result.append(w.node.start)
        result.extend(w)

def generate_ith_graph(
    line_no : int, line_mapping : dict[int, Type[Block]],
    top_level : list[int], whiles : Stack[While]
):
    """Generate the execution graph up to the ith line.
    Return a list of raw line numbers to show in the graph."""
    if whiles:
        while whiles:
            top : While = whiles.peek()
            node : WhileBlock = top.node
            if line_no == node.start:


            if line_no == node.start or line_no > node.end:
                break
            whiles.pop()

    if 
