from collections import OrderedDict
import inspect
from typing import Callable

from cfg import OFFSET

def get_code_info(program : Callable):
    lines, start = inspect.getsourcelines(program)
    start += OFFSET
    return OrderedDict(
        (line_no, line_contents) for line_no, line_contents in enumerate(
            lines[OFFSET:], start=start
        )
    )

def find_first_nospace(string : str):
    """a crude way of finding the first non-space character"""
    for i, s in enumerate(string):
        if not s.isspace():
            return i
    return len(string)

def get_leading_whitespace(string : str):
    return string[:find_first_nospace(string)]

def num_leading_whitespace(string : str):
    return len(get_leading_whitespace(string))

def get_stripped_line(string : str):
    return string[find_first_nospace(string):]

def uniq(mapping : OrderedDict[int, bool]):
    """Remove all consecutive False keys with the first occuring one"""
    filtered : OrderedDict[int, bool] = OrderedDict()
    prev_false = False
    for index, value in mapping.items():
        if value or not prev_false:
            filtered[index] = value
            prev_false = not value
    
    return filtered
