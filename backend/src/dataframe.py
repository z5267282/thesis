from counter import Counter

def DataFrame():
    def __init__(
        self,
        code : list[str], lines : list[str], curr : int,
        variables : dict[str, str], out : list[str],
        path : list[int], counters : list[Counter], evalbox : list[str]
    ):
        self.code : list[str] = code
        self.lines : list[str] = lines
        self.curr : int = curr
        self.vars : dict[str, str] = variables
        self.out : list[str] = out
        self.counters = counters
        self.evalbox = evalbox
    
    def to_dict(self):
        pass
