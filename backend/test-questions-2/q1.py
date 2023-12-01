HI = 100_000
i, j, k = 0, 1, 2
while i + j + k <= HI:
    name = "boat"
    if i % j == 0:
        name = "bubble"
    elif (j + k) % 3 == 1:
        name = "fish"
    elif (k - i) % 7 > j % 4:
        name = "spider"
    
    if k * i < j * 23:
        entity = "inc"
    elif i % 5 == (j + k) % 5:
        entity = "llc"
    else:
        entity = "pty ltd"
    
    company = f"{name} {entity}."
    print(f"choice : {company}")
    i += j
    j += k
    k = (i + j) + (2 * k) % 14
print("that's all")
