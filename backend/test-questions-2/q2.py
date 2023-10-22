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
