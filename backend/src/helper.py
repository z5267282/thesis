import re

def find_first_nospace(string):
    '''a crude way of finding the first non-space character'''
    for i, s in enumerate(string):
        if not s.isspace():
            return i
    return len(string)

def get_leading_whitespace(string):
    return string[:find_first_nospace(string)]

# string = '    hello'
# string = ''
# space = get_leading_whitespace(string)
# print("|{}|".format(space))
