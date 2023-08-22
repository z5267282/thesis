i = 1
twos, fives = 0, 0
while i < 6:
    if i % 2 == 0:
        print("two")
        twos += 1
    elif i % 5 == 0:
        print("five")
        fives += 1
    
    total = 0
    j = 0
    while j <= i:
        total += j
        j += 1

    print(f"sum 0..{i} = {total}")
    i += 1
    
print(f"2s: {twos}, 5s: {fives}")
