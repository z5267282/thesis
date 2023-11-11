from dataclasses import dataclass
from typing import Any

@dataclass
class Last:
    """A class to store the last line of program state.
    Note that the sys.settrace wrapper cannot directly return values."""
    variables : dict[str, Any]
    output    : list[str]

l = Last({1 : 2}, ["hello"])
print(*l)
