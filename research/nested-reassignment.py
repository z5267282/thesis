class Top:
    def __init__(self, x):
        self.x = x

def A():
    t = Top(1)
    B(t)
    print(t.x)

def B(t):
    t = Top(2)

A()
