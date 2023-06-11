import json
from typing import List, Type, Union

class Block():
    def __init__(self, start : int):
        self.start    : int = start
        self.end      : int = None

    def __dict__(self):
        return {
            self.__class__.__name__ : {
                "start" : self.start,
                "end"   : self.end
            }
        }

class CodeBlock(Block):
    pass

# putting this here because it apparently can't be a class variable
ForwardReferenceOptionalBody = Union['BodyBlock', CodeBlock]
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
        self.else_ : None | ElseBlock = None

class ElifBlock(BodyBlock):
    """separate this so that the IfBlock tracks the entire branch structure"""
    pass

class ElseBlock(BodyBlock):
    """made a class to differentiate from BodyBlock"""
    pass

# type aliases
BodyBlockDescendant = Type[BodyBlock]
OptionalBodyBlock   = BodyBlock | Block
ConditionalBlock    = IfBlock | ElifBlock | ElseBlock
