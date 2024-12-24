from typing import Generic, TypeVar

T = TypeVar("T")

class State(Generic[T]):
    """dataclass to track previous and current state"""
    def __init__(self, prev : T, curr : T=None) -> None:
        self.prev : T = prev
        self.curr : T = curr

    def __eq__(self, other : "State") -> bool:
        return self.prev == other.prev and self.curr == other.curr

    def __ne__(self, other : "State") -> bool:
        return not self == other
