from collections import deque
from typing import Deque, Type

from tree import BodyBlock

class Stack:
    """a simple wrapper around deque"""
    def __init__(self, root : BodyBlock):
        self.items : Deque[Type[BodyBlock]] = deque()
        self.push(root)
    
    def __str__(self):
        """print items from top to bottom"""
        # note a deque stores items in insertion order
        return "\n".join(
            f"{i} : {block}" 
                for i, block in enumerate(reversed(self.items), start=1)
        )

    def __len__(self):
        return len(self.items)
    
    def empty(self):
        return len(self) == 0
    
    def peek(self):
        """retrive the top item without removing it

        method according to the documentation here:
        https://docs.python.org/3/library/collections.html#collections.deque"""
        return self.items[-1]

    def pop(self):
        """remove the top item and return it"""
        return self.items.pop()
    
    def pop_peek(self):
        """remove the top item and return the new top"""
        self.pop()
        return self.peek()
    
    def push(self, item : Type[BodyBlock]):
        self.items.append(item)
