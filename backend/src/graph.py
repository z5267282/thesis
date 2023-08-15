from collections import namedtuple

from line import Line
from stack import Stack
from tree import WhileBlock

class While:
    def __init__(self, node : WhileBlock):
        self.node  : WhileBlock = node
        self.lines : list[int] = []

def generate_line_execution_graph(index : int, filtered : list[Line], top_level : list[int]):
    
