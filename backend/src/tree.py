from collections import OrderedDict
import json
from typing import Any, Type, Union

class Block():
    def __init__(self, start : int, indent_level : int) -> None:
        self.start        : int = start
        self.end          : int = None
        self.indent_level : int = indent_level
    
    def __str__(self) -> str:
        """Simply print the block without recursive unpacking"""
        return "{}(start={}, end={})".format(
            self.__class__.__name__, self.start, self.end
        )
    
    def __repr__(self):
        return str(self)

    def to_dict(self) -> dict[str, int]:
        return {
            self.__class__.__name__ : {
                "start" : self.start,
                "end"   : self.end
            }
        }
    
    def map_lines(self) -> dict[int, Type["Block"]]:
        line_mapping : dict[int, Type["Block"]] = {}
        for i in range(self.start, self.end + 1):
            line_mapping[i] = self
        return line_mapping
    
    def show_lines(
        self, graph : list[int], show : OrderedDict[int, bool]
    ) -> None:
        for i in range(self.start, self.end + 1):
            show[i] = True
    
    def is_conditional(self) -> bool:
        """Verify whether the current node is a conditional block.
        Conditional blocks have an expression associated with them"""
        return False

    def pretty_print(self) -> None: # pragma: no cover
        """A pretty printer for debugging"""
        print(json.dumps(self.to_dict(), indent=2))

class CodeBlock(Block):
    pass

class BodyBlock(Block):
    """For storing a succession of blocks on the same indetation level"""
    def __init__(self, start: int, indent_level : int) -> None:
        super().__init__(start, indent_level)
        self.body       : list[Type["BodyBlock"] | CodeBlock] = []
        # for storing the most recent code block
        self.code_block : CodeBlock | None = None
    
    def to_dict(self) -> dict[str, Any]:
        parent = super().to_dict()
        parent[self.__class__.__name__]["body"] = [
            b.to_dict() for b in self.body
        ]
        return parent
    
    def map_lines(self) -> dict[int, Type[Block]]:
        parent : dict[int, Type[Block]] = super().map_lines()
        for b in self.body:
            parent.update(b.map_lines())
        return parent
    
    def show_lines(
        self, graph : list[int], show : OrderedDict[int, bool]
    ) -> None:
        for b in self.body:
            b.show_lines(graph, show)
    
    def part_of(self, graph : list[int]) -> bool:
        return self.start in graph and graph[-1] != self.start

    def add_same_level_block(
        self, block : Type["BodyBlock"] | CodeBlock
    ) -> None:
        self.body.append(block)
    
    def end_code_block(self, end : int) -> None:
        """End the code block if set"""
        if self.code_block is None:
            return

        self.code_block.end = end
        self.code_block = None

class ConditionalBlock(BodyBlock):
    def is_conditional(self) -> bool:
        return True

class WhileBlock(ConditionalBlock):
    def show_lines(
        self, graph: list[int], show: OrderedDict[int, bool]
    ) -> None:
        show[self.start] = True
        if self.part_of(graph):
            super().show_lines(graph, show)

class ElifBlock(ConditionalBlock):
    """Separate this so that the IfBlock tracks the entire branch structure"""
    pass

class ElseBlock(ConditionalBlock):
    def is_conditional(self) -> bool:
        """An else block does not have an expression attached to it"""
        return False

class IfBlock(ConditionalBlock):
    """The if block must lay out on the same nesting level:
    any elifs, and an else"""
    def __init__(self, start: int, indent_level : int) -> bool:
        super().__init__(start, indent_level)
        self.elifs : list[ElifBlock] = []
        self.else_ : None | ElseBlock = None

    def to_dict(self) -> dict[str, Any]:
        parent : dict[str, Any] = super().to_dict()
        parent[self.__class__.__name__]["elifs"] = [
            el.to_dict() for el in self.elifs
        ]
        parent[self.__class__.__name__]["else"] = \
            None if self.else_ is None else self.else_.to_dict()
        return parent
    
    def map_lines(self) -> dict[int, Type[Block]]:
        parent : dict[int, Type[Block]] = super().map_lines()
        for e in self.elifs:
            parent.update(e.map_lines())
        if self.else_ is not None:
            parent.update(self.else_.map_lines())
        return parent
    
    def show_lines(
        self, graph: list[int], show: OrderedDict[int, bool]
    ) -> None:
        # recursive order doesn't matter:
        # can find then recurse, or the other way around :)
        show[self.start] = True
        if self.part_of(graph): 
            super().show_lines(graph, show)
        for e in self.elifs:
            show[e.start] = True
            if e.part_of(graph):
                e.show_lines(graph, show)
        if self.else_ is not None:
            show[self.else_.start] = True
            if self.else_.part_of(graph):
                self.else_.show_lines(graph, show)
    
    def add_elif(self, elif_block : ElifBlock) -> None:
        self.elifs.append(elif_block)
    
    def add_else(self, else_block : ElseBlock) -> None:
        self.else_ = else_block
    
    def find_branch(
        self, line_no : int
    ) ->Union["IfBlock" , ElifBlock , ElseBlock]:
        """Find which branch starts at a given line number if any"""
        if line_no == self.start:
            return self
        
        for e in self.elifs:
            if line_no == e.start:
                return e

        return self.within_else(line_no)    
    
    def within_else(self, line_no : int) -> bool:
        """Determine whether a given line number is within an else block.
        Return the start of the else block if within bounds, otherwise None."""
        if self.else_ is None:
            return None
        
        bounded : bool = (
            line_no >= self.else_.start
            and line_no <= self.else_.end
        )
        return self.else_ if bounded else None
    
class FunctionBlock(BodyBlock):
    def __init__(self, start: int, indent_level : int, name : str):
        super().__init__(start, indent_level)
        self.name : str = name
    
    def show_lines(self, graph : list[int], show : OrderedDict[int, bool]):
        show[self.start] = True
        if self.part_of(graph):
            super().show_lines(graph, show)
