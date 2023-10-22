YEAR = 2023
N = 10_000
i = 0
print(f"some facts about the numbers up to {N}")
while i < N:
    if i % 2 == 0 and i % 7 == 0:
        print(f"fancy fourteen")
        i += 1
    elif i % 3 and i % 7 and i * i > 4 * i:
        print("a 21 whose square is larger than its quadruple")
        i += 2
    elif i % 3221 == 0 and i % 7727 == 3:
        print("secret")
        i += 4
    elif i % 47 and i > YEAR:
        print("a 47 after this year")
        i += 8
    elif i % 53 == 0 and i % 977 == 0:
        print("a big prime")
        i += 16
    i += 32
print("the end")