from collections import OrderedDict
from typing import Any, Callable

from counter import Counter
from tree import WhileBlock

class Line:
    """A dataclass to store line information"""
    def __init__(self, line_no : int, variables : dict[str, Any]=None) -> None:
        self.line_no   : int = line_no
        self.output    : list[str] = []
        self.variables : dict[str, Any] = {} if variables is None else variables
        # counters are stored from least indented to most indented
        self.counters  : list[Counter] = []
    
    def __repr__(self) -> str: # pragma: no cover
        """Return a simple representation to assist with debugging asserts."""
        return str(self.line_no)
    
    def __eq__(self, other : "Line") -> bool:
        return self.line_no == other.line_no

    def __ne__(self, other : "Line") -> bool:
        return not self == other
    
    @staticmethod
    def display_lines(lines : list["Line"]) -> str: # pragma: no cover
        """A debugging method to format a list of lines for printing"""
        return ", ".join(str(line.line_no) for line in lines)
    
    def long_str(self) -> str:
        delim    : str = ",\n{}".format(" " * 8)
        counters : str = """
        {}
    """.format(
            delim.join(str(counter) for counter in self.counters)
        ) if self.counters else ""

        dict_to_str : Callable = lambda dic: ", ".join(
            f"{key} : {value}" for key, value in dic.items()
        )

        return f"""line {self.line_no}:
    output : [{", ".join(str(o) for o in self.output)}]
    vars : {{{dict_to_str(self.variables)}}}
    counters : [{counters}]"""

    def fix_lag(self, output : list[str], variables : dict[str, Any]) -> None:
        """Fix a line so that it has the right state.
        This is based on the limitaton of sys.settrace which runs lines
        as they are entered, not as they are left."""
        self.output.extend(output)
        self.variables.update(variables)
    
    def add_counter(
        self, iteration : int, total : int, while_ : WhileBlock
    ) -> None:
        """Add a counter of an increased depth"""
        self.counters.append(Counter(iteration, total, while_))
    
    def range_filter_counters(self, filtered : OrderedDict[int, bool]) -> None:
        for counter in self.counters:
            counter.find_filtered_range(filtered, self.line_no)
