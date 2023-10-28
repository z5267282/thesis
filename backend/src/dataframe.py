from copy import deepcopy
from typing import Any

from counter import Counter
from state import State

class DataFrame:
    def __init__(
        self,
        code : list[str], lines : list[str], curr : int | None,
        variables : State[dict[str, Any]], out : list[str],
        path : list[int], counters : list[Counter], evalbox : list[str]
    ):
        self.code  : list[str] = deepcopy(code)
        self.lines : list[str] = deepcopy(lines)
        self.curr  : int = curr

        self.variables : State[dict[str, Any]] = variables

        self.out : list[str] = deepcopy(out)

        self.path     : list[int] = deepcopy(path)
        self.counters : list[Counter] = deepcopy(counters)
        self.evalbox  : list[str] = deepcopy(evalbox)
    
    def to_dict(self):
        path = {
            "start" : 0,
            "rest"  : self.generate_rest()
        }

        variables : list[dict] = [
            {
                "name"    : name,
                "value"   : str(value),
                "changed" : (
                    name not in self.variables.prev
                    or self.variables.prev[name] != value
                )
            } for name, value in sorted(self.variables.curr.items())
        ]

        counters = [
            counter.to_dict() for counter in self.counters \
            if counter.has_valid_range()
        ]

        return {
            "code"     : self.code,
            "lines"    : self.lines,
            "curr"     : self.curr,
            "vars"     : variables,
            "out"      : self.out,
            "path"     : path,
            "counters" : counters,
            "evalbox"  : self.evalbox
        }
    
    def generate_rest(self) -> list[int]:
        """Generate the remaining path ensuring that it does not start with 0"""
        if not self.path:
            return []
        
        if self.path[0] == 0:
            return self.path[1:]
        
        return self.path
