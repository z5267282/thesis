class Bad(Exception):
    def __init__(self):
        super().__init__("bad thing happened")

raise Bad
