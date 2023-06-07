class ElifParseError(Exception):
    def __init__(self):
        super().__init__("an elif block was parsed without a same level if first")

class ElseParseError(Exception):
    def __init__(self):
        super().__init__("an else block was parsed without a same level if first")

class UnsupportedIndentation(Exception):
    def __init__(self):
        super().__init__("an indentation involving an unsupported code feature was wirtten")
