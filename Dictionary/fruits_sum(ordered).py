#sum of values 
from collections import OrderedDict
d = {}
n = int(input())
for i in range(n):
    a = input().split(' ')
    key = ' '.join(a[:-1])
    if key in d:
        d[key] += int(a[-1])
    else:
        d[key] = int(a[-1])

d = OrderedDict(sorted(d.items(), key=lambda x: x[0]))
for i in d.items():
    print(i[0], i[1])
