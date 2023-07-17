class Line:
    """A dataclass to store line information"""
    def __init__(self, line_no : int, output : list[str], ):
        self.line_no   : int = line_no
        self.output    : list[str] = output
        self.prev_vars : dict[str, str] = 
        self.curr_vars : 
    
    def __str__(self):
        return "the output is: @{}@".format(", ".join(self.output))
        # return f"{self.line_no} : {self.locals}"
        # return f"lno: {self.line_no}, out: '{self.out}'"
