from typing import List

class Block():
    def __init__(self, start : int):
        self.start : int = start
        self.end   : int = None

class CodeBlock(Block):
    pass

class BodyBlock(Block):
    def __init__(self, start: int):
        super().__init__(start)
        self.body : List[BodyBlock | Block] = []
    
class WhileBlock(BodyBlock):
    pass

class ElifBlock(BodyBlock):
    pass

class IfBlock(BodyBlock):
    def __init__(self, start: int):
        super().__init__(start)
        self.elifs : List[IfBlock] = []
        # must call it this because else is a reserved word
        self.else_ : None | BodyBlock = None
