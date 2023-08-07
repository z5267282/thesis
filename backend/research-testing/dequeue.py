from collections import deque

def append():
    d = deque()
    d.append(1)
    print(len(d))

def extendleft():
    d = deque()
    ls = [1, 2, 3]
    ls.reverse()
    d.extendleft(ls)
    print(", ".join(str(i) for i in d))

extendleft()
