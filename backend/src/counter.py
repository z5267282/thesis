from tree import WhileBlock

class Counter:
    """A dataclass to store counter information"""
    def __init__(self, iteration : int, total : int, while_ : WhileBlock):
        self.iteration = iteration
        self.total = total
        self.while_ = while_
    
    def __str__(self):
        return f"({self.iteration}/{self.total}) : {self.while_}"
    
    def __eq__(self, other : "Counter"):
        return self.iteration == other.iteration and self.total == other.total

    def __ne__(self, other : "Counter"):
        return not self == other
