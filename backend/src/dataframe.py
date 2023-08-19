from copy import deepcopy

from counter import Counter

class DataFrame:
    def __init__(
        self,
        code : list[str], lines : list[str], curr : int | None,
        variables : dict[str, str], out : list[str],
        path : list[int], counters : list[Counter], evalbox : list[str]
    ):
        self.code  : list[str] = code
        self.lines : list[str] = lines
        self.curr  : int = curr

        self.vars  : list[str] = [
            f"{name} = {value}" for name, value in variables.items()
        ]

        self.out : list[str] = deepcopy(out)
        self.out.reverse()

        self.path     : list[int] = path
        self.counters : list[Counter] = counters
        self.evalbox  : list[str] = evalbox
    
    def to_dict(self):
        path = {
            "start" : 0,
            "rest"  : self.path
        }

        counters = [
            counter.to_dict() for counter in self.counters \
            if counter.has_valid_range()
        ]

        return {
            "code"     : self.code,
            "lines"    : self.lines,
            "curr"     : self.curr,
            "vars"     : self.vars,
            "out"      : self.out,
            "path"     : path,
            "counters" : counters,
            "evalbox"  : self.evalbox
        }
