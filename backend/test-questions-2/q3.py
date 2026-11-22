j, k = 2, 4
while j < 100:
    if j % 3 + k % 3 == 3:
        a, b, = j, k
        while b != 0:
            a, b = b, a % b
        print(f"the gcd of {j} and {k} is {a}")
    elif j % 5 > (k + 1) % 4:
        i, total = 1, 0
        while i <= k:
            if i % 2 == 0:
                total += 1
            i += 1
        print(f"sum evens to {k} is {total}")
    elif j * k > k ** 2:
        i = 0
        while i < 5:
            print("X" * 5)
            i += 1
    j += 1
    k += j
print("end of program")