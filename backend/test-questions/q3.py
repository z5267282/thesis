i = 0
GRID = 5
while i < 3000:
    if i % 17 == 0:
        j = 0
        while j < GRID:
            k = 0
            while k < GRID:
                if j == k:
                    print("X", end="")
                else:
                    print("O", end="")
                k += 1
            print("")
            j += 1
    elif i % 29 == 0 and i % 73 == 0:
        j = 0
        while j < GRID:
            k = 0
            while k < GRID:
                if j + k == GRID - 1:
                    print("X", end="")
                else:
                    print("O", end="")
                k += 1
            print("")
            j += 1
    print("-" * GRID)
    i += 1