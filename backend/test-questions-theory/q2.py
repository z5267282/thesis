n = 2 ** 3 * 5 ** 12 * 7 ** 8 * 11 ** 3
print(n)

while n % 2 == 0:
    n //= 2
while n % 3 == 0:
    n //= 3


print(n)
