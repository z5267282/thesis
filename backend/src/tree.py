class Block():
    def __init__(self, start, end):
        self.start = start
        self.end = end

class AssignmentBlock(Block):
    def __init__(self, start, end):
        super.__init__(start, end)
