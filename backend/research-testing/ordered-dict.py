from collections import OrderedDict

o = OrderedDict((i, False) for i in range(10))

for oi in o.items():
    print(oi)
