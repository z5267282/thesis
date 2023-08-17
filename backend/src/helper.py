from collections import OrderedDict

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

def uniq(show : OrderedDict[int, bool]):
    """Remove all consecutive False keys with the first occuring one"""
    filtered : OrderedDict[int, bool] = OrderedDict()
    prev_false = False
    for line, shown in show.items():
        if shown or not prev_false:
            filtered[line] = shown
            prev_false = False
    
    return filtered
