class ExistingElseError(Exception):
    def __init__(self):
        super().__init__("there is already an else block for an if block")

class ExpectedIfBlock(Exception):
    def __init__(self):
        super().__init__("an if block was expected during parsing")
