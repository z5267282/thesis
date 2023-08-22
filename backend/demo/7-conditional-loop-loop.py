i = 0
while i < 4:
    if i % 2 == 0:
        row = ""
        j = i
        while j >= 0:
            row = f"{row} {j}"
            j -= 1
        print(row)
    else:
        row = ""
        j = 0
        while j <= i:
            row = f"{row} {j}"
            j += 1
        print(row)
    i += 1
print("the end!")