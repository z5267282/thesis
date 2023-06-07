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
    
    def __len__(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        """method according to the documentation here:
        https://docs.python.org/3/library/collections.html#collections.deque"""
    
        return self.items[-1]

def init_tree():
    # for now assume program is only top level code
    lines, start = inspect.getsourcelines(program)
    root = BodyBlock(start + 1)
    root.end = len(lines)
    return root
