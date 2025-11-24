class State[T]():
    """dataclass to track previous and current state"""

    def __init__(self, prev: T, curr: T = None) -> None:
        self.prev: T = prev
        self.curr: T = curr

    def __eq__(self, other: object) -> bool:
        if isinstance(other, State):
            return self.prev == other.prev and self.curr == other.curr
        return False

    def __ne__(self, other: object) -> bool:
        return not self == other
