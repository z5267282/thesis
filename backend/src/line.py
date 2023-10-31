from collections import OrderedDict
from typing import Any

from counter import Counter
from state import State
from tree import WhileBlock

class Line:
    """A dataclass to store line information"""
    def __init__(self, line_no : int, variables : dict[str, Any]={}):
        self.line_no   : int = line_no
        self.output    : list[str] = []
        self.variables : dict[str, Any] = variables
        # counters are stored from least indented to most indented
        self.counters  : list[Counter] = []
    
    def __repr__(self): # pragma: no cover
        """Return a simple representation to assist with debugging asserts."""
        return str(self.line_no)
    
    def __eq__(self, other : "Line"):
        return self.line_no == other.line_no

    def __ne__(self, other : "Line"):
        return not self == other
    
    @staticmethod
    def display_lines(lines : list["Line"]):
        """A debugging method to format a list of lines for printing"""
        return ", ".join(str(line.line_no) for line in lines)
    
    def long_str(self):
        delim = ",\n{}".format(" " * 8)
        counters : str = """
        {}
    """.format(
            delim.join(str(counter) for counter in self.counters)
        ) if self.counters else ""

        dict_to_str = lambda dic: ", ".join(
            f"{key} : {value}" for key, value in dic.items()
        )

        return f"""line {self.line_no}:
    output : [{", ".join(str(o) for o in self.output)}]
    vars : {{{dict_to_str(self.variables)}}}
    counters : [{counters}]"""
    
    def add_counter(self, iteration : int, total : int, while_ : WhileBlock):
        """Add a counter of an increased depth"""
        self.counters.append(Counter(iteration, total, while_))
    
    def range_filter_counters(self, filtered : OrderedDict[int, bool]):
        for counter in self.counters:
            counter.find_filtered_range(filtered, self.line_no)
