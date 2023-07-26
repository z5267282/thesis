from state import State

class Line:
    """A dataclass to store line information"""
    def __init__(self, line_no : int, prev_vars : dict[str, str]):
        self.line_no : int = line_no
        self.output  : list[str] = []
        self.vars    : State = State(prev_vars)
    
    def __str__(self):
        return str(self.line_no)
    
    def long_print(self):
        return f"""line no {self.line_no}:
    output: {self.output}
    vars  :
        - prev: {self.vars.prev}
        - curr: {self.vars.curr}"""

    def __eq__(self, other):
        return self.line_no == other.line_no
