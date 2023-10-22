HI = 100_000
i, j, k = 0, 1, 2
while i + j + k <= HI:
    name = "boat"
    if i % j == 0:
        name = "bubble"
    elif j + k % 57 == 13:
        name = "fish"
    elif k - i > 91:
        name = "spider"
    
    if (k * i) % j == 23:
        entity = "inc"
    elif k % 42 == 1:
        entity = "llc"
    else:
        entity = "pty ltd"
    
    company = f"{name} {entity}."
    print(f"choice : {company}")
    i += j
    j += k
    k = (i + j) + (2 * k) % 14

print("that's all")
