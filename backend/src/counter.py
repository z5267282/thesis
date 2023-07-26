from fractions import Fraction

from tree import WhileBlock

class Counter:
    """A dataclass to store counter information"""
    def __init__(self, iteration : Fraction, while_ : WhileBlock):
        self.iteration = iteration
        self.while_ = while_
    
    def __str__(self):
        return "line {} - ({}/{})".format(
            self.while_, self.iteration.numerator, self.iteration.denominator
        )
