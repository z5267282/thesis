from collections import OrderedDict
from typing import Type

from line import Line
from tree import Block, BodyBlock, CodeBlock, IfBlock

def filter(graph : list[int], root : BodyBlock):
    """Return a list of n booleans where n is the number of lines in a
    program where the ith boolean is whether the ith line is to be shown"""
    # 1-indexed to make life easy
