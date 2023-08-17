from collections import OrderedDict

from counter import Counter
from state import State
from tree import WhileBlock

class Line:
    """A dataclass to store line information"""
    def __init__(self, line_no : int, prev_vars : dict[str, str]):
        self.line_no   : int = line_no
        self.output    : list[str] = []
        self.vars      : State[dict[str, str]] = State(prev_vars)
        # counters are stored from least indented to most indented
        self.counters  : list[Counter] = []
    
    def __str__(self):
        return str(self.line_no)
    
    def __repr__(self):
        return f"Line({self.line_no})"
    
    def __eq__(self, other : "Line"):
        return self.line_no == other.line_no

    def __ne__(self, other : "Line"):
        return not self == other
    
    def long_str(self):
        delim = ",\n{}".format(" " * 8)
        counters : str = """
        {}
    """.format(
            delim.join(str(counter) for counter in self.counters)
        ) if self.counters else ""

        dict_to_str = lambda dic: ", ".join(
            f"{key} : {dic[key]}" for key in dic
        )

        return f"""line {self.line_no}:
    output: [{", ".join(str(o) for o in self.output)}]
    vars  :
        - prev: {{{dict_to_str(self.vars.prev)}}}
        - curr: {{{dict_to_str(self.vars.curr)}}}
    counters: [{counters}]"""
    
    def add_counter(self, iteration : int, total : int, while_ : WhileBlock):
        """Add a counter of an increased depth"""
        self.counters.append(Counter(iteration, total, while_))
    
    def range_filter_counters(self, filtered : OrderedDict[int, bool]):
        for counter in self.counters:
            counter.find_filtered_range(filtered)
