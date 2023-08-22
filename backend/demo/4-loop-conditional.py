i = 1
twos, fives = 0, 0
while i < 6:
    if i % 2 == 0:
        print("two")
        twos += 1
    elif i % 5 == 0:
        print("five")
        fives += 1
    i += 1

print(f"2s: {twos}, 5s: {fives}")