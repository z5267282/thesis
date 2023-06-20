class ElifParseError(Exception):
    def __init__(self):
        super().__init__("an elif block was parsed without a same level if first")

class ElseParseError(Exception):
    def __init__(self):
        super().__init__("an else block was parsed without a same level if first")

class NoEnclosingIfError(Exception):
    def __init__(self, is_elif : bool):
        super().__init__(
            "there is no enclosing if block for an {}".format(
                "elif" if is_elif else "else"
            )
        )

class ExistingElseError(Exception):
    def __init__(self):
        super().__init__("there is already an else block for an if block")
