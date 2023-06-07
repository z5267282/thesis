from collections import deque
import inspect

from program import program
from tree import BodyBlock

class State:
    def __init__(self):
        self.is_first     : bool = True
        self.indent_level : int = None
        self.start        : int = None
        self.end          : int = None

class Stack:
    """a simple wrapper around deque"""

    def __init__(self):
        self.items = deque()

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

def init_tree():
    # for now assume program is only top level code
    lines, start = inspect.getsourcelines(program)
    root = BodyBlock(start + 1)
    root.end = len(lines)
    return root
