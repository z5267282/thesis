from collections import deque
from typing import Generic, Type, TypeVar

T = TypeVar("T")

class Stack(Generic[T]):
    """A simple wrapper around deque"""

    def __init__(self, first : T=None):
        self.items : deque[Type[T]] = deque()
        if first is not None:
            self.push(first)
    
    def __str__(self):
        """Print items from top to bottom"""
        return "\n".join(
            f"{i} : {block}" 
                # note a deque stores items in insertion order
                for i, block in enumerate(reversed(self.items), start=1)
        )

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)
    
    def empty(self):
        return len(self) == 0
    
    def peek(self):
        """Retrive the top item without removing it.
        Method according to the documentation here:
        https://docs.python.org/3/library/collections.html#collections.deque"""
        return self.items[-1]

    def pop(self):
        """Remove the top item and return it"""
        return self.items.pop()
    
    def pop_peek(self):
        """Remove the top item and return the new top"""
        self.pop()
        return self.peek()
    
    def push(self, item : Type[T]):
        self.items.append(item)
