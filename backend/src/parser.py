from collections import deque
import inspect
from typing import Deque, Type

from program import program
from tree import BodyBlock, BodyBlockDescendant, OptionalBodyBlock

class State:
    """a dataclass to store any necessary information during parsing
    used as the function to sys.settrace can only take in one helper argument"""
    def __init__(self, root : BodyBlock):
        self.indent_level : int = None
        self.start        : int = None
        self.end          : int = None
        self.filename     : str = inspect.getsourcefile(program)
        # the root must be a BodyBlock, because you don't know how to add nested blocks
        self.root         : BodyBlock = root
        self.stack        : Stack = Stack(root)

class Stack:
    """a simple wrapper around deque"""
    def __init__(self, root : BodyBlock):
        self.items : Deque[BodyBlockDescendant] = deque()
        self.push(root)
    
    def __len__(self):
        return len(self.items)

    def push(self, item : OptionalBodyBlock):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        """method according to the documentation here:
        https://docs.python.org/3/library/collections.html#collections.deque"""
        return self.items[-1]

def init_state():
    root : BodyBlock = init_root()
    return State(root)

def init_root():
    # for now assume program is only top level code
    lines, start = inspect.getsourcelines(program)
    root = BodyBlock(start + 1)
    root.end = len(lines)
    return root
