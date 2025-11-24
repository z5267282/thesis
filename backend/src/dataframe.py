from copy import deepcopy
from typing import Any

from counter import Counter
from state import State

class DataFrame:
    def __init__(
        self,
        code : list[str], lines : list[str], curr : int | None,
        variables : State[dict[str, Any]],
        out : list[str], path : list[int], counters : list[Counter],
        evalbox : list[str]
    ) -> None:
        self.code  : list[str] = deepcopy(code)
        self.lines : list[str] = deepcopy(lines)
        self.curr  : int | None = curr

        # variables from the previous and current DataFrame
        self.variables : State[dict[str, Any]] = variables

        self.out : list[str] = deepcopy(out)

        self.path     : list[int] = deepcopy(path)
        self.counters : list[Counter] = deepcopy(counters)
        self.evalbox  : list[str] = deepcopy(evalbox)
    
    def to_dict(self) -> dict[str, Any]:
        path : dict[str, int | list[int]] = {
            "start" : 0,
            "rest"  : self.generate_rest()
        }

        variables = [
            {
                "name"    : variable,
                "value"   : str(value),
                "changed" : self.is_changed(variable) 
            } for variable, value in sorted(self.variables.curr.items())
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
        """Generate the remaining path ensuring that it does not start with 0.
        Note, it should have already generated properly from collapse()"""
        if not self.path:
            return []
        
        # possible for the first frame to be also the first line
        # eg. a code block starting and ending at line 1
        if self.path[0] == 0:
            return self.path[1:]
        
        return self.path
    
    def is_changed(self, variable : str) -> bool:
        """Check if a current variable has changed by the time the current line
        has run.
        The change could be from the previous DataFrame, or presently."""
        if variable not in self.variables.prev:
            return True
        
        return self.variables.prev[variable] != self.variables.curr[variable]
    
    @staticmethod
    def to_dicts(dataframes : list["DataFrame"]) -> list[dict[str, Any]]:
        """Convert each DataFrame in a list to a dictionary and return the
        list."""
        return [ d.to_dict() for d in dataframes ] 
