class Line:
    """A dataclass to store line information"""
    def __init__(self, line_no : int, locals : dict, output : list[str]):
        self.line_no : int = line_no
        self.locals  : dict = locals
        self.output  : list[str] = output
    
    def __str__(self):
        return "the output is: @{}@".format(", ".join(self.output))
        # return f"{self.line_no} : {self.locals}"
        # return f"lno: {self.line_no}, out: '{self.out}'"
