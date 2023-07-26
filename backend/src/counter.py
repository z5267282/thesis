from tree import WhileBlock

class Counter:
    """A dataclass to store counter information"""
    def __init__(self, iteration : int, total : int, while_ : WhileBlock):
        self.iteration = iteration
        self.total = total
        self.while_ = while_
    
    def __str__(self):
        return "({}/{}) : {}".format(
            self.iteration.numerator, self.iteration.denominator,
            self.while_.start
        )
