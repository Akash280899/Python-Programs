#repeated words and its occurences
from collections import OrderedDict
d = OrderedDict()
for i in range(int(input())):
    a = input()
    d.setdefault(a, 0)
    d[a] += 1
   
print(len(d))
print(*d.values())
