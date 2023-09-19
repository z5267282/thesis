class C:
    def __init__(self, x):
        self.x = x
    
    def __str__(self):
        return str(self.x)

ls = [C(1)]
top = ls[-1]
top.x = 50

for c in ls:
    print(c)
