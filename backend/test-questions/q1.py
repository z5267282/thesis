i = 1
while i < 12345:
    if i % 7841 == 0 and i % 23 == 0:
        i += 3
    elif i > 3000:
        i += 2
    else:
        i += 43
print("that's all folks")
