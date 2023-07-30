from typing import Any

class State:
    """dataclass to track previous and current state"""
    def __init__(self, prev : Any, curr : Any=None):
        self.prev : Any = prev
        self.curr : Any = curr

    def __eq__(self, other : "State"):
        return self.prev == other.prev and self.curr == other.curr

    def __ne__(self, other : "State"):
        return not self == other
