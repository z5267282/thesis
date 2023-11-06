X, Y, Z = 7, 4, 3

i = 0
while i < X:
    print("--X--", end="")
    j = 0
    while j < Y:
        print("!Y!", end="")
        k = 0
        while k < Z:
            print("Z", end="")
            k += 1

        j += 2

    print(" ", end="")
    i += 3

print("done")
