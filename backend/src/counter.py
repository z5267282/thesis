from collections import OrderedDict

from tree import WhileBlock

class Counter:
    """A dataclass to store counter information"""
    def __init__(self, iteration : int, total : int, while_ : WhileBlock):
        self.iteration : int = iteration
        self.total     : int = total
        self.while_    : WhileBlock = while_
        self.start     : int | None = None
        self.end       : int | None = None
    
    def __str__(self):
        return f"({self.iteration}/{self.total}) : {self.while_}"
    
    def __eq__(self, other : "Counter"):
        return self.iteration == other.iteration and self.total == other.total

    def __ne__(self, other : "Counter"):
        return not self == other

    def find_filtered_range(
        self, filtered : OrderedDict[int, bool], curr_line : int
    ):
        """Set the start and ending ranges for a counter if it appears in a
        line filtering."""
        keys = list(filtered)
        index = keys.index(self.while_.start)
        
        # we are current executing the while the counter is tracking
        # display statistics info
        if self.while_.start == curr_line:
            self.start = index
            self.end = index + 1

        self.start = index
        # note the lines should be in non-decreasing order
        for i, key in enumerate(keys[index:], start=index):
            if key > self.while_.end:
                break

            self.end = i
        # after the loop terminates, i should be the largest index:
        # 1. key[i] <= while end
        # 2. consecutive from index

        # possible that self.start is None, but not self.end
        # this will be considered invalid later

    def has_valid_range(self):
        if self.start is None or self.end is None:
            return False
        return True
    
    def to_dict(self):
        return {
            "start"       : self.start,
            "end"         : self.end,
            "numerator"   : self.iteration,
            "denominator" : self.total
        }
