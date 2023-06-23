import json
from typing import List, Type, Union

from errors import ExistingElseError

class Block():
    def __init__(self, start : int):
        self.start    : int = start
        self.end      : int = None
    
    def __str__(self):
        """simply print the block without recursive unpacking"""
        return "{}(start={}, end={})".format(
            self.__class__.__name__, self.start, self.end
        )

    def to_dict(self):
        return {
            self.__class__.__name__ : {
                "start" : self.start,
                "end"   : self.end
            }
        }

    def pretty_print(self):
        """a pretty printer for debugging"""
        print(json.dumps(self.to_dict(), indent=2))

class CodeBlock(Block):
    pass

# putting this here because it apparently can't be a class variable
# pipe syntax does not work for forward references so use Union
ForwardReferenceOptionalBody = Union[Type['BodyBlock'], CodeBlock]
class BodyBlock(Block):
    """for storing a succession of blocks on the same indetation level"""
    def __init__(self, start: int, indent_level : int):
        super().__init__(start)
        self.body         : List[ForwardReferenceOptionalBody] = []
        # for storing the most recent code block
        self.code_block   : CodeBlock | None                   = None
        self.indent_level : int                                = indent_level
    
    def add_same_level_block(self, block : ForwardReferenceOptionalBody):
        self.body.append(block)
    
    def to_dict(self):
        parent = super().to_dict()
        parent[self.__class__.__name__]["body"] = [b.to_dict() for b in self.body]
        return parent
    
    def end_code_block(self, end : int):
        """end the code block if set"""
        if self.code_block is None:
            return

        self.code_block.end = end
        self.code_block = None

class WhileBlock(BodyBlock):
    pass

# put these here for type hints in the if block

class ElifBlock(BodyBlock):
    """separate this so that the IfBlock tracks the entire branch structure"""
    pass

class ElseBlock(BodyBlock):
    """made a class to differentiate from BodyBlock"""
    pass

class IfBlock(BodyBlock):
    """the if block must lay out on the same nesting level:
    any elifs, and an else"""
    def __init__(self, start: int, indent_level : int):
        super().__init__(start, indent_level)
        self.elifs : List[ElifBlock] = []
        self.else_ : None | ElseBlock = None

    def to_dict(self):
        parent = super().to_dict()
        parent[self.__class__.__name__]["elifs"] = [el.to_dict() for el in self.elifs]
        parent[self.__class__.__name__]["else"] = \
            None if self.else_ is None else self.else_.to_dict()
        return parent
    
    def add_elif(self, elif_block : ElifBlock):
        self.elifs.append(elif_block)
    
    def add_else(self, else_block : ElseBlock):
        if self.else_ is not None:
            raise ExistingElseError

        self.else_ = else_block
