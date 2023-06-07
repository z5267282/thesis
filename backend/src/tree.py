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

class IfBlock(BodyBlock):
    """the if block must lay out on the same nesting level:
    any elifs, and an else"""
    def __init__(self, start: int):
        super().__init__(start)
        self.elifs : List[ElifBlock] = []
        self.else_ : None | BodyBlock = None

class ElifBlock(BodyBlock):
    """separate this so that the IfBlock tracks the entire branch structure"""
    pass
