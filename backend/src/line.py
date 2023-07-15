class Line:
    """A dataclass to store line information"""
    def __init__(self, line_no : int, locals : dict, out : list[str]):
        self.line_no : int = line_no
        self.locals  : dict = locals
        self.out     : list[str] = out
    
    def __str__(self):
        return str(self.line_no)
        # return f"{self.line_no} : {self.locals}"
        # return f"lno: {self.line_no}, out: '{self.out}'"
