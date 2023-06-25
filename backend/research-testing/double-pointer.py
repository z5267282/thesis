# test to see if a reference nested in 2 function calls can be globally used

class C:
    def __init__(self, x):
        self.x = x

def main():
    c = C(10)
    a(c)
    print(c.x)

def a(c):
    c.x = 13
    b(c)

def b(c):
    c.x = 42

main()
