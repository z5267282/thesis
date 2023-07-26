from fractions import Fraction

from tree import WhileBlock

class Counter:
    """A dataclass to store counter information"""
    def __init__(self, iteration : Fraction, while_ : WhileBlock):
        self.iteration = iteration
        self.while_ = while_
