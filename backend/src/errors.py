class ElifParseError(Exception):
    def __str__(self):
        return "an elif block was parsed without a same level if first"

class ElseParseError(Exception):
    def __str__(self):
        return "an else block was parsed without a same level if first"

class UnsupportedIndentation(Exception):
    def __str__(self):
        return "an indentation involving an unsupported code feature was wirtten"
