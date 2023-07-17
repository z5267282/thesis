from state import State

class Line:
    """A dataclass to store line information"""
    def __init__(
            self, line_no : int, output : list[str],
            prev : dict[str, str], curr : dict[str, str]
    ):
        self.line_no : int = line_no
        self.output  : list[str] = output
        self.vars    : State = State(prev, curr)
    
    def __str__(self):
        return "the output is: @{}@".format(", ".join(self.output))
        # return f"{self.line_no} : {self.locals}"
        # return f"lno: {self.line_no}, out: '{self.out}'"
