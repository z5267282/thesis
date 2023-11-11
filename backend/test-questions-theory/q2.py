n = 14986230724609375000
p = n

two = True
while p % 2 == 0:
    p //= 2
    two = not two

if two:
    while p % 3 == 0:
        p //= 3
else:
    five = False
    while p % 5 == 0:
        p //= 5
        five = not five

    if not five:
        while p % 7 == 0:
            p //= 7
    else:
        while p % 11:
            p //= 11
