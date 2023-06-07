from typing import List, Type, Union

class Block():
    def __init__(self, start : int):
        self.start : int = start
        self.end   : int = None

class CodeBlock(Block):
    pass

# putting this here because it apparently can't be a class variable
ForwardReferenceOptionalBody = Union['BodyBlock', Block]

class BodyBlock(Block):

    def __init__(self, start: int):
        super().__init__(start)
        self.body : List[ForwardReferenceOptionalBody] = []
    
    # pipe syntax does not work for forward references so use Union
    def add_same_level_block(self, block : ForwardReferenceOptionalBody):
        self.body.append(block)
    
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

class ElifParseError(Exception):
    """when an elif block is parsed without a same level if first"""
    pass

class ElseParseError(ElifParseError):
    """consider an else to be a type of elif for heirachy simplicity"""
    pass

BodyBlockDescendant = Type[BodyBlock]
OptionalBodyBlock = BodyBlock | Block
