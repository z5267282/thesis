i, twos, fives = 1, 0, 0
while i < 98765:
    if i % 2047 == 1648:
        print("what a special day it is!")
    elif i % 2 == 0:
        print("two")
        twos += 1
    elif i % 5 == 0:
        print("five")
        fives += 1
    total = 0
    j = 1
    while j <= i:
        total += j
        j += 1
    print(f"sum 1..{i} = {total}")
    i += i + i % 53
    
print(f"2s: {twos}, 5s: {fives}")