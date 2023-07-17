from typing import Any

class State:
    """dataclass to track previous and current state"""
    def __init__(self, prev : Any):
        self.prev : Any = prev
        self.curr : Any = None
