class State:
    """dataclass to track previous and current state"""
    def __init__(self, prev : any, curr: any):
        self.prev : any = prev
        self.curr : any = curr
