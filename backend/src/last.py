from typing import Any

class Last:
    """A class to store the last line of program state in execute.
    We cannot use a Line object for this since there is not always a meaningful
    last line of execution.
    It is mainly used in the sys.settrace wrapper as we cannot directly return
    values and must work on external state."""
    def __init__(self):
        self.variables : dict[str, Any] = {}
        self.output    : list[str] = []
