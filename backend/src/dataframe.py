from copy import deepcopy
from typing import Any

from counter import Counter
from state import State

class DataFrame:
    def __init__(
        self,
        code : list[str], lines : list[str], curr : int | None,
        variables : State[dict[str, Any]], out : list[str],
        path : list[int], start : int | None,
        counters : list[Counter], evalbox : list[str], call : dict | None
    ):
        self.code  : list[str] = deepcopy(code)
        self.lines : list[str] = deepcopy(lines)
        self.curr  : int | None = curr

        # variables from the previous and current DataFrame
        self.variables : State[dict[str, Any]] = variables

        self.out : list[str] = deepcopy(out)

        self.start    : int | None = start
        self.path     : list[int] = deepcopy(path)
        self.counters : list[Counter] = deepcopy(counters)
        self.evalbox  : list[str] = deepcopy(evalbox)

        self.call : dict | None = call
    
    def to_dict(self):
        path = None if self.start is None else \
            {
                "start" : self.start,
                "rest"  : self.transform_rest()
            }

        variables : list[dict] = [
            {
                "name"    : variable,
                "value"   : str(value),
                "changed" : self.is_changed(variable) 
            } for variable, value in sorted(self.variables.curr.items())
        ]

        counters : list[Counter] = [
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
            "evalbox"  : self.evalbox,
            "call"     : self.call
        }
    
    def transform_rest(self):
        """Manipulate the rest attribute so it is ready for conversion to a dict"""
        fixed_start : list[int] = self.generate_rest()

        # remove duplicate return values now
        if len(fixed_start) < 2:
            return fixed_start
        
        if fixed_start[-1] == fixed_start[-2]:
            return fixed_start[:-1]
        
        return fixed_start

    def generate_rest(self) -> list[int]:
        """Generate the remaining path ensuring that it does not start with 0.
        Note, it should have already generated properly from collapse()"""
        if not self.path:
            return []
        
        # possible for the first frame to be also the first line
        # eg. a code block starting and ending at line 1
        if self.path[0] == self.start:
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
