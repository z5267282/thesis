HI = 10_000
i, j, k = 0, 1, 2
while i + j + k <= HI:
    name = "boat"
    if i % j == 0:
        name = "bubble"
    elif j + k % 57 == 13:
        name = "fish"
    elif k - i > 91:
        name = "spider"
    
    city = "Sydney"
    a, b, rem = j, k, k % j
    while rem != 0:
        a = b
        b = rem
        rem = a % b
    if rem % 4 == 0:
        city = "Brisbane"
    elif rem % 7 == 3:
        city = "Melbourne"
    
    entity = ""
    if (rem * i) % j == 23:
        entity = "inc"
    elif rem % 42 == 1:
        entity = "llc"
    else:
        entity = "pty ltd"
    
    print(f"congratulations on founding : {name} {city} {entity}.")
    i += j
    j += k
    k = (i + j) + (2 * k) % 14
