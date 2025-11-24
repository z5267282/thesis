from typing import Iterator


class Stack[T]:
    """A LIFO data structure"""

    def __init__(self) -> None:
        self.items: list[T] = []

    def __str__(self) -> str:
        """Print items from top to bottom"""
        return "\n".join(
            f"{i} : {block}"
            # note a deque stores items in insertion order
            for i, block in enumerate(reversed(self.items), start=1)
        )

    def __len__(self) -> int:
        return len(self.items)

    def __iter__(self) -> Iterator[T]:
        return iter(self.items)

    def empty(self) -> bool:
        return len(self) == 0

    def peek(self) -> T:
        """Retrive the top item without removing it.
        Method according to the documentation here:
        https://docs.python.org/3/library/collections.html#collections.deque"""
        return self.items[-1]

    def pop(self) -> T:
        """Remove the top item and return it"""
        return self.items.pop()

    def pop_peek(self) -> T:
        """Remove the top item and return the new top"""
        self.pop()
        return self.peek()

    def push(self, item: T) -> None:
        self.items.append(item)
