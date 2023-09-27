from copy import deepcopy
from typing import Any

from counter import Counter

class DataFrame:
    def __init__(
        self,
        code : list[str], lines : list[str], curr : int | None,
        variables : dict[str, Any], out : list[str],
        path : list[int], counters : list[Counter], evalbox : list[str]
    ):
        self.code  : list[str] = deepcopy(code)
        self.lines : list[str] = deepcopy(lines)
        self.curr  : int = curr

        self.vars  : list[str] = [
            f"{name} = {value}" for name, value in variables.items()
        ]

        self.out : list[str] = deepcopy(out)
        # self.out.reverse()

        self.path     : list[int] = deepcopy(path)
        self.counters : list[Counter] = deepcopy(counters)
        self.evalbox  : list[str] = deepcopy(evalbox)
    
    def to_dict(self):
        path = {
            "start" : 0,
            "rest"  : self.generate_rest()
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
    
    def generate_rest(self):
        """Generate the remaining path ensuring that it does not start with 0"""
        if not self.path:
            return self.path
        
        if self.path[0] == 0:
            return self.path[1:]
        
        return self.path
