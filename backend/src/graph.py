from collections import namedtuple

from line import Line
from stack import Stack
from tree import BodyBlock, WhileBlock

class While:
    def __init__(self, node : WhileBlock):
        self.node  : WhileBlock = node
        self.lines : list[int] = []
    
def generate_ith_graph(
    line_no : int, root : BodyBlock,
    top_level : list[int], whiles : Stack[While]
):
    if whiles:
        while whiles:
            top : While = whiles.peek()
            node : WhileBlock = top.node
            if line_no == node.start or line_no > node.end:
                break
            whiles.pop()

    if 