import typing

class Block():
    def __init__(self, start : int):
        self.start : int = start
        self.end   : int = None

class CodeBlock(Block):
    pass

class BodyBlock(Block):
    def __init__(self, start: int):
        super().__init__(start)
        self.body : typing.List[Block] = []

class WhileBlock(BodyBlock):
    pass

class IfBlock(BodyBlock):
    def __init__(self, start: int):
        super().__init__(start)
        self.elifs : typing.List[IfBlock] = []
        # must call it this because else is a reserved word
        self.else_ : None | BodyBlock = None
