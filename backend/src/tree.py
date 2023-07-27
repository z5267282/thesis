import json
from typing import Type

class Block():
    def __init__(self, start : int):
        self.start : int = start
        self.end   : int = None
    
    def __str__(self):
        """Simply print the block without recursive unpacking"""
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
    
    def map_lines(self, ):
        line_mapping : dict[int, Type["Block"]] = {}
        for i in range(self.start, self.end + 1):
            line_mapping[i] = self
        return line_mapping

    def pretty_print(self):
        """A pretty printer for debugging"""
        print(json.dumps(self.to_dict(), indent=2))

class CodeBlock(Block):
    pass

class BodyBlock(Block):
    """For storing a succession of blocks on the same indetation level"""
    def __init__(self, start: int, indent_level : int):
        super().__init__(start)
        self.body         : list[Type["BodyBlock"] | CodeBlock] = []
        # for storing the most recent code block
        self.code_block   : CodeBlock | None = None
        self.indent_level : int = indent_level
    
    def get_top(self):
        """Return the top most block in body"""
        return self.body[0]
    
    def to_dict(self):
        parent = super().to_dict()
        parent[self.__class__.__name__]["body"] = [
            b.to_dict() for b in self.body
        ]
        return parent
    
    def map_lines(self, ):
        parent : dict[int, Type[Block]] = super().map_lines()
        for b in self.body:
            parent.update(b.map_lines())
        return parent
    
    def add_same_level_block(self, block : Type["BodyBlock"] | CodeBlock):
        self.body.append(block)
    
    def end_code_block(self, end : int):
        """End the code block if set"""
        if self.code_block is None:
            return

        self.code_block.end = end
        self.code_block = None

class WhileBlock(BodyBlock):
    pass

# put these here for type hints in the if block

class ElifBlock(BodyBlock):
    """Separate this so that the IfBlock tracks the entire branch structure"""
    pass

class ElseBlock(BodyBlock):
    """Made a class to differentiate from BodyBlock"""
    pass

class IfBlock(BodyBlock):
    """The if block must lay out on the same nesting level:
    any elifs, and an else"""
    def __init__(self, start: int, indent_level : int):
        super().__init__(start, indent_level)
        self.elifs : list[ElifBlock] = []
        self.else_ : None | ElseBlock = None

    def to_dict(self):
        parent = super().to_dict()
        parent[self.__class__.__name__]["elifs"] = [
            el.to_dict() for el in self.elifs
        ]
        parent[self.__class__.__name__]["else"] = \
            None if self.else_ is None else self.else_.to_dict()
        return parent
    
    def map_lines(self, ):
        parent : dict[int, Type[Block]] = super().map_lines()
        for e in self.elifs:
            parent.update(e.map_lines())
        if self.else_ is not None:
            parent.update(self.else_.map_lines())
        return parent
    
    def add_elif(self, elif_block : ElifBlock):
        self.elifs.append(elif_block)
    
    def add_else(self, else_block : ElseBlock):
        self.else_ = else_block
    
    def find_branch(self, line_no : int):
        """Find which branch starts at a given line number if any"""
        if line_no == self.start:
            return self
        
        for e in self.elifs:
            if line_no == e.start:
                return e
        
        if self.else_ is not None and line_no == self.else_.start:
            return self.else_
        
        return None
